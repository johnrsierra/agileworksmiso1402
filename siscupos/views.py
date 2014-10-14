from django.shortcuts import render,HttpResponse
from siscupos.models import Asignatura,AsignaturaSugerida,AsignaturaXEstudiante,AsignaturaXPrograma,Estudiante,PreAsignacionCurso,PreProgramacion,ProgramaAcademico
from django.shortcuts import render_to_response
from django.template import RequestContext
import json
from django.core import serializers
from SolverAsignacion import *

# Create your views here.
def index(request):
    programas = ProgramaAcademico.objects.count()
    estudiantes = Estudiante.objects.count()
    materias = Asignatura.objects.count()
    ejecuciones=PreAsignacionCurso.objects.count()
    context = {'nuevos_programas':programas,'nuevos_estudiantes':estudiantes,'nuevas_materias':materias,'ejecuciones':ejecuciones}
    return render(request,'index.html', context)

def coordinacion(request):
    lista_programas = ProgramaAcademico.objects.all()
    context = {'lista_programas':lista_programas}
    return render(request,'coordinacion/lista_programas.html',context)

def consultarPreProgramacion(request,prog_id):
    if prog_id is not None:
        programa = ProgramaAcademico.objects.get(pk=prog_id)
        lista_programacion = PreProgramacion.objects.filter(asignaturaXPrograma__programaAcademico=prog_id)
        context={'lista_programacion':lista_programacion,'programa':programa}
        return render(request,'coordinacion/plan_programa.html',context)
    else:
        return render(request,'coordinacion/plan_programa.html',{})

#Retorna el listado de materias
def materias(request):
    lista_materias = Asignatura.objects.all()
    context = {'lista_materias':lista_materias}
    return render(request,'materias/lista_materias.html',context)

#Retorna el listado de estudiantes
def estudiantes(request):
    lista_estudiantes = Estudiante.objects.all()
    context = {'lista_estudiantes':lista_estudiantes}
    return render(request,'estudiantes/lista_estudiantes.html',context)

#Lista los cursos que han sido seleccionados por los estudiantes y aun no han sido cursados
#Cursados -> 0 no ha sido cursado
#            1 ya fue cursado
def demandaCupos(request):
    lista_demanda = Asignatura.demanda_cupos()
    context = {'lista_demanda':lista_demanda}
    return render(request,'coordinacion/demanda.html',context)

def ejecuciones(request):
    lista_programas = ProgramaAcademico.objects.all()
    lista_ejecuciones = PreAsignacionCurso.objects.all()
    context = {'lista_ejecuciones':lista_ejecuciones,'lista_programas':lista_programas}
    return render(request,'coordinacion/optimizador.html',context)

def resultado(request,preasig_id):
    if preasig_id is not None:
        preAsignacionCurso = PreAsignacionCurso.objects.get(pk=preasig_id)
        lista_resultado = preAsignacionCurso.asignaturasugerida_set.all()
        contexto = {'edit':False,'preProg':preAsignacionCurso,'lista_resultado':lista_resultado}
        return render(request,'coordinacion/resultado_ejecucion.html',contexto)
    else:
        return render(request,'contactos/resultado_ejecucion.html',{})

def jsonTest(request):
    asig = Asignatura.objects.all()
    data = serializers.serialize('json',asig, fields=('plan'))
    return HttpResponse(data, content_type='application/json; charset=UTF-8')

def optimizando(request):
    optimizarAutomatico()
    context = {}
    return render(request,'coordinacion/optimizando.html',context)

def carpeta(request,est_id):
    #debe ser la lista de materias del programa del estudiante
    est = Estudiante.objects.get(pk=est_id)
    periodos = darPeriodos(est.periodoInicio)
    mats_periodos = []
    for x in range(0,len(periodos)):
        lista_materias = AsignaturaXEstudiante.objects.filter(estudiante=est,periodo=periodos[x])
        mats_periodos.append({'periodo':periodos[x],'lista_materias':lista_materias})
    context = {'estudiante':est,'periodos':periodos,'mats_periodos':mats_periodos}
    return render(request,'estudiantes/carpeta.html',context)

#Este metodo deberia eliminarse y traer los periodos de la DB
def darPeriodos(periodo):
    ano = str(periodo[:4])
    sem = str(periodo[-2:])
    periodos = []
    periodos.append(periodo)
    for x in range(1,4):
        if(sem == '10'):
            sem = '20'
        else:
            ano = str(int(ano)+1)
            sem = '10'
        per = ano + sem
        periodos.append(per)
    return periodos

from django.db import connection

def consultarAsignacionPrograma(request, prog,corrida):
    cursor = connection.cursor()
    cursor.execute('select  asisug."preAsignacionCurso_id", pro."sigla" plan, asig."codigo" asignatura,"seccion" seccion,count(*) estudiantes, max(cupos) cupos from  siscupos_preasignacioncurso preasig,siscupos_asignaturasugerida asisug,siscupos_preprogramacionasig pre,siscupos_asignaturaxprograma asi,siscupos_programaacademico pro,siscupos_asignatura asig where preasig.id = %s and pro.sigla = %s and asisug."preAsignacionCurso_id" = preasig.id and pre."preProgramacion_id" = asisug."preProgramacion_id" and pre."asignaturaXPrograma_id" = asi.id and pre."preAsignacionCurso_id" = preasig.id and pro.id = asi."programaAcademico_id" and asig.id = asi."asignatura_id" group by asisug."preAsignacionCurso_id",pro."sigla",asig."codigo", seccion order by 1',[corrida,prog])
    cursos = cursor.fetchall()
    results = []
    for row in cursos:
        p = {'id':row[0],'programa':row[1],'asignatura':row[2],'seccion':row[3],'estudiantes':row[4],'cupos':row[5]}
        results.append(p)

    return HttpResponse(json.dumps(results), content_type='application/json; charset=UTF-8')

#FSandoval: consulta para conocer la satisfaccion de los estudiantes en una corrida dada
def consultarSatisfaccionPrograma(request, corrida):
    #Variables que contienen los resultados
    porcentajeUno = 0
    porcentajedos = 0
    results = []

    #consulta los resultados de los estudiantes que inscribieron un curso
    cursorUno = connection.cursor()
    cursorUno.execute('select CAST(AVG(case when COALESCE(a.asignadas,0)= COALESCE(b.capacidad,0) THEN 100 ELSE 0 end) as integer) , count(*) estudiantes from (select count(*) asignadas, asig.estudiante_id estudiante from siscupos_asignaturasugerida asig where asig."preAsignacionCurso_id" = %s group by asig.estudiante_id ) a RIGHT OUTER JOIN (select count(*) capacidad, estudiante_id estudiante from siscupos_asignaturaxestudianteasig asig where estado = \'0\'  and asig."preAsignacionCurso_id" = %s group by estudiante_id) b ON  b.estudiante = a.estudiante where b.capacidad = 1', [corrida, corrida])
    resultadoUno = cursorUno.fetchall()
    for row in resultadoUno:
        porcentajeUno = row[0]

    #consulta los resultados de los estudiantes que inscribieron dos cursos
    cursordos = connection.cursor()
    cursordos.execute('select CAST(AVG(case when COALESCE(a.asignadas,0)= 2 THEN 100 WHEN COALESCE(a.asignadas,0)= 1 THEN 50 ELSE 0 end) as integer), count(*) estudiantes from (select count(*) asignadas, asig.estudiante_id estudiante from siscupos_asignaturasugerida asig where asig."preAsignacionCurso_id" = %s group by asig.estudiante_id ) a RIGHT OUTER JOIN (select count(*) capacidad, estudiante_id estudiante from siscupos_asignaturaxestudianteasig asig where estado = \'0\' and asig."preAsignacionCurso_id" = %s group by estudiante_id) b ON  b.estudiante = a.estudiante where b.capacidad > 1', [corrida, corrida])
    resultadodos = cursordos.fetchall()

    for row in resultadodos:
        porcentajedos = row[0]

    #Carga los resultados en un objeto JSon
    p1 = {'tipo': '1', 'porcentaje': porcentajeUno}
    p2 = {'tipo': '2', 'porcentaje': porcentajedos}
    results.append(p1)
    results.append(p2)

    return HttpResponse(json.dumps(results ), content_type='application/json; charset=UTF-8')