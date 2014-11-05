from django.shortcuts import render,HttpResponse
from siscupos.models import Asignatura,AsignaturaSugerida,AsignaturaXEstudiante,AsignaturaXPrograma,Estudiante,PreAsignacionCurso,PreProgramacion,ProgramaAcademico
from django.shortcuts import render_to_response
from django.template import RequestContext
import json
from django.core import serializers
from AsignadorCupos import *
from django.shortcuts import render,HttpResponse
from siscupos.models import Asignatura,AsignaturaSugerida,AsignaturaXEstudiante,AsignaturaXPrograma,Estudiante,PreAsignacionCurso,PreProgramacion,ProgramaAcademico
from django.shortcuts import render_to_response
from django.template import RequestContext
import json
from django.core import serializers
from AsignadorCupos import *

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
    lista_ejecuciones_comp = PreAsignacionCurso.objects.all()
    context = {'lista_ejecuciones':lista_ejecuciones,'lista_programas':lista_programas, 'lista_ejecuciones_comp':lista_ejecuciones_comp}
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
    solver = AsignadorCupos()
    solver.poblar_estudiantesBD('201410')
    asignacion_sugerida = solver.asignacion_optima()
    solver.persistirResultado(asignacion_sugerida, '201410')
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

def micarpeta(request,est_id):
    #debe ser la lista de materias del programa del estudiante
    est = Estudiante.objects.get(pk=est_id)
    periodos = darPeriodos(est.periodoInicio)

    # Obtiene las asignaturas del estudiante
    lista_materias = AsignaturaXPrograma.objects.filter(programaAcademico=est.programa)
    mats_periodos = []

    #Consulta las materias que fueron asignadas por el optimizador en su ultima corrida
    preAsignacionCurso_id = PreAsignacionCurso.objects.order_by('-id')[0]

    for x in range(0,len(periodos)):
        # Consulta el listado de asignaturas preasignadas
        lista_materias_preasignadas = AsignaturaSugerida.objects.filter(estudiante=est, preAsignacionCurso=preAsignacionCurso_id)
        mats_periodos_asig = []

        #Recorre el listado de preasignacion y ubica las materias q corresponde al periodo que se esta consultando
        for materiasAsig in lista_materias_preasignadas:
            perAsig = materiasAsig.preAsignacionCurso.periodo

            if perAsig == periodos[x]:
                mats_periodos_asig.append(materiasAsig)

        #Consulta las asignaturas que el estudiante tiene en el periodo
        lista_materias_periodo = AsignaturaXEstudiante.objects.filter(estudiante=est,periodo=periodos[x])

        cursor = connection.cursor()
        cursor.execute(
            'select asig.id, asig.cursada, asig.estado, asig.asignatura_id, asi.codigo, asig.estudiante_id, asig.periodo '
            'FROM siscupos_asignaturaxestudianteasig asig '
            'INNER JOIN siscupos_asignatura asi ON asi.id = asig.asignatura_id '
            'WHERE '
            'asig.periodo like \'' + str(periodos[x]) + '\' and asig.estudiante_id = ' + str(est_id) +
            ' and asig."preAsignacionCurso_id" = (select max("preAsignacionCurso_id") from siscupos_asignaturaxestudianteasig)')
        cursos = cursor.fetchall()
        results = []
        for row in cursos:
            p = {'id':row[0],'cursada':row[1],'estado':row[2],'asignatura_id':row[3],'asignatura_codigo':row[4],'estudiante_id':row[5],'periodo':periodos[x]}
            results.append(p)

        print('results', results)
        print('periodos[x]', periodos[x])

        #Asigna las asignaturas del periodo y las sugeridas por el optimizador
        mats_periodos.append({'periodo':periodos[x],'lista_materias_periodo':lista_materias_periodo, 'lista_materias_asignadas': mats_periodos_asig, 'lista_asig_est_asig': results})
    context = {'estudiante':est,'periodos':periodos,'lista_materias':lista_materias,'mats_periodos':mats_periodos}
    return render(request,'estudiante/carpeta.html',context)

def nuevacarpeta(request,est_id):
    #debe ser la lista de materias del programa del estudiante
    est = Estudiante.objects.get(pk=est_id)

    print('<<<<Actualizar carpeta>>>')

    if request.is_ajax():
        if request.method == 'POST':
            print 'Raw Data: "%s"' % request.body

    #Obtiene los datos enviados
    idEstudiante = request.POST['idEstudiante']
    nuevasMaterias = request.POST.getlist('nuevaMaterias[]')
    borrarMaterias = request.POST.getlist('borraMaterias[]')


    print('<<<<nuevasMaterias>>>', nuevasMaterias)
    print('<<<<borrarMaterias>>>', borrarMaterias)


    #Recorre el listado de las materias a borrar
    for matBorrar in borrarMaterias:
        #Extrae el periodo
        codPeriodo = matBorrar[(matBorrar.find("---")) + 3 :]
        print('<<<<codPeriodo>>>', codPeriodo)
        #Extraer el codigo de la materia
        codMateria = matBorrar[:(matBorrar.find("---"))]
        print('<<<<codMateria>>>', codMateria)

        try:
            #Busca la asignatura
            objAsig = Asignatura.objects.get(codigo=codMateria)
            print('<<<<objAsig>>>', objAsig)
            #Busca el estudiante
            objEst = Estudiante.objects.get(pk=idEstudiante)
            print('<<<<objEst>>>', objEst)
            #Busca la asignatura x estudiante
            objAsigXEst = AsignaturaXEstudiante.objects.get(asignatura=objAsig, estudiante=objEst)
            print('<<<< Asignatura x Estudiante a Borrar >>>', objAsigXEst)
            #Ejecuta el borrado del registro
            objAsigXEst.delete()
        except AsignaturaXEstudiante.DoesNotExist:
            print('<<<<No se puede borrar>>>', objAsig, ',', objEst)

    #Recorre el listado de las materias a asignar
    for matNueva in nuevasMaterias:

        codPeriodo = matNueva[(matNueva.find("---")) + 3 :]
        codMateria = matNueva[:(matNueva.find("---"))]

        try:
            #Busca la asignatura
            objAsig = Asignatura.objects.get(codigo=codMateria)
            #Busca el estudiante
            objEst = Estudiante.objects.get(pk=idEstudiante)
            #Busca la asignatura x estudiante
            objAsigXEst = AsignaturaXEstudiante.objects.get(asignatura=objAsig.pk, estudiante=idEstudiante)
        except AsignaturaXEstudiante.DoesNotExist:
            #Si no existe la asignatura x estudiante crea el registro
            objAsigXEst_nuevo = AsignaturaXEstudiante(cursada='N', estado='0', asignatura=objAsig, estudiante=objEst, periodo=codPeriodo)
            print('<<<< Asignatura x Estudiante a Crear >>>', objAsigXEst_nuevo)
            objAsigXEst_nuevo.save()

    return render(request,'estudiante/carpeta.html')


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

def demandaxasignacion(request,corrida):
    cursor = connection.cursor()
    cursor.execute('select COALESCE(a.asignadas,0) asignadas, COALESCE(b.capacidad,0) demanda, b.asignatura_id, b.asignatura from (select  asisug."preAsignacionCurso_id", pro."sigla" plan, asig."codigo" asignatura,asig.id asignatura_id,count(*) asignadas from  siscupos_preasignacioncurso preasig,siscupos_asignaturasugerida asisug,siscupos_preprogramacionasig pre,siscupos_asignaturaxprograma asi,siscupos_programaacademico pro,siscupos_asignatura asig where preasig.id= %s and asisug."preAsignacionCurso_id" = preasig.id and pre."preProgramacion_id" = asisug."preProgramacion_id" and pre."asignaturaXPrograma_id" = asi.id and pre."preAsignacionCurso_id" = preasig.id and pro.id = asi."programaAcademico_id" and asig.id = asi."asignatura_id" group by asisug."preAsignacionCurso_id",pro."sigla",asig."codigo",asig.id) a RIGHT OUTER JOIN (select count(*) capacidad,asig.asignatura_id,asg.codigo asignatura from siscupos_asignaturaxestudianteasig asig,siscupos_asignatura asg where asig.estado = \'0\' and asig."preAsignacionCurso_id" = %s and asg.id = asig."asignatura_id" group by asignatura_id,asg.codigo ) b ON a.asignatura_id = b.asignatura_id',[corrida,corrida])
    demanda = cursor.fetchall()
    results = []
    for row in demanda:
        p = {'asignadas':row[0],'demanda':row[1],'asignatura_id':row[2],'asignatura':row[3]}
        results.append(p)

    return HttpResponse(json.dumps(results), content_type='application/json; charset=UTF-8')

def indicadoresDetalleSatis(request,corrida):
    print('Iniciio indicadores Detalle')
    cursor = connection.cursor()
    dataA = []
    resultsHC = []


    # Indicador 1: Porcentaje de cupos asignados
    cursor.execute(
        ' select c.satisfaccion, count(*) '
        ' from ( '
        ' select (case when COALESCE(b.capacidad,0) >= 2 and COALESCE(a.asignadas,0)= 2 THEN 100 '
        ' when COALESCE(b.capacidad,0) >= 2 and COALESCE(a.asignadas,0)= 1 THEN 50 '
        ' when COALESCE(b.capacidad,0) >= 2 and COALESCE(a.asignadas,0)= 0 THEN 0 '
        ' when COALESCE(b.capacidad,0) >= 1 and COALESCE(a.asignadas,0)= 1 THEN 100 '
        ' when COALESCE(b.capacidad,0) >= 1 and COALESCE(a.asignadas,0)= 0 THEN 0 '
        ' else 0 end) satisfaccion '
        ' ,a.asignadas '
        ' ,b.capacidad '
        ' ,b.estudiante '
        ' from (select count(*) asignadas, asig.estudiante_id estudiante, asig."preAsignacionCurso_id" corrida '
        ' from siscupos_asignaturasugerida asig '
        ' where asig."preAsignacionCurso_id" = %s '
        ' group by asig.estudiante_id,asig."preAsignacionCurso_id" '
        ' order by 3,2 ) a '
        ' RIGHT OUTER JOIN  '
        ' (select count(*) capacidad, estudiante_id estudiante, asig."preAsignacionCurso_id" corrida '
        ' from siscupos_asignaturaxestudianteasig asig '
        ' where estado = \'0\'   '
        ' and asig."preAsignacionCurso_id" = %s '
        ' group by estudiante_id, asig."preAsignacionCurso_id" '
        ' order by 3,2) b '
        ' ON  b.estudiante = a.estudiante '
        ' AND b.corrida = a.corrida) c '
        ' group by c.satisfaccion '
        ' order by c.satisfaccion   ',
        [corrida, corrida]
    )

    print('antes de fetchall de detalle Satis' + corrida)
    cupos = cursor.fetchall()
    for row in cupos:
        print('recorriendo cupos ', row[1])
        dataA.append(int(row[1]))

    phcA ={'name':'Corrida '+str(corrida), 'data':dataA}

    resultsHC.append(phcA)
    print(resultsHC)

    httpResp = HttpResponse(json.dumps(resultsHC), content_type='application/json; charset=UTF-8')

    print('antes de return')
    return httpResp



def indicadoresDetalleEstudiantes(request,corrida, porc_satisfaccion):
    print('Iniciio indicadores Detalle estudiante')
    cursor = connection.cursor()
    dataA = []


    # Indicador 1: Porcentaje de cupos asignados
    cursor.execute(
        ' select codigo, nombres, apellidos, estudiante '
        ' from ( '
        ' select (case when COALESCE(b.capacidad,0) >= 2 and COALESCE(a.asignadas,0)= 2 THEN 100 '
        ' when COALESCE(b.capacidad,0) >= 2 and COALESCE(a.asignadas,0)= 1 THEN 50 '
        ' when COALESCE(b.capacidad,0) >= 2 and COALESCE(a.asignadas,0)= 0 THEN 0 '
        ' when COALESCE(b.capacidad,0) >= 1 and COALESCE(a.asignadas,0)= 1 THEN 100 '
        ' when COALESCE(b.capacidad,0) >= 1 and COALESCE(a.asignadas,0)= 0 THEN 0 '
        ' else 0 end) satisfaccion '
        ' ,a.asignadas '
        ' ,b.capacidad '
        ' ,b.estudiante estudiante '
        ' ,b.nombres nombres, b.apellidos apellidos, b.codigo codigo '
        ' from (select count(*) asignadas, asig.estudiante_id estudiante, asig."preAsignacionCurso_id" corrida '
        ' from siscupos_asignaturasugerida asig '
        ' where asig."preAsignacionCurso_id" = %s '
        ' group by asig.estudiante_id,asig."preAsignacionCurso_id" '
        ' order by 3,2 ) a '
        ' RIGHT OUTER JOIN  '
        ' (select count(*) capacidad, '
        '         estudiante_id estudiante, '
        '         asig."preAsignacionCurso_id" corrida, '
        '         est.nombres, est.apellidos, est.codigo '
        ' from siscupos_asignaturaxestudianteasig asig '
        '     ,siscupos_estudiante est '
        ' where estado = \'0\'   '
        ' and asig.estudiante_id = est.id '
        ' and asig."preAsignacionCurso_id" = %s '
        ' group by estudiante_id, asig."preAsignacionCurso_id", est.nombres, est.apellidos, est.codigo '
        ' order by 3,2) b '
        ' ON  b.estudiante = a.estudiante '
        ' AND b.corrida = a.corrida '
        ' ) c '
        ' where c.satisfaccion = %s ',
        [corrida, corrida, porc_satisfaccion]
    )

    print('antes de fetchall de detalle Satis' + corrida)
    cupos = cursor.fetchall()
    for row in cupos:
        e = Estudiante()
        e.codigo = row[0]
        e.nombres = row[1]
        e.apellidos = row[2]
        e.id = row[3]
        print('recorriendo estudientas ', row[1])
        dataA.append(e)

    print('antes de return')
    context = {'lista_estudiantes':dataA}
    return render(request,'estudiantes/lista_estudiantes.html',context)







def indicadores(request,corridaA, corridaB):
    print('Iniciio indicadores')
    cursor = connection.cursor()
    results = []
    dataA = []
    dataB = []

    # Indicador 1: Porcentaje de cupos asignados
    cursor.execute(
        ' select  round((sum(a.estudiantes)/sum(a.cupos))*100), a.corrida '
        ' from( '
        ' select  asisug."preAsignacionCurso_id" corrida '
        ' , pro."sigla" plan '
        ' , count(*) estudiantes '
        ' , max(cupos) cupos '
        ' from  siscupos_preasignacioncurso preasig '
        '      ,siscupos_asignaturasugerida asisug '
        '      ,siscupos_preprogramacionasig pre '
        '      ,siscupos_asignaturaxprograma asi '
        '      ,siscupos_programaacademico pro '
        '      ,siscupos_asignatura asig '
        ' where preasig.id in (%s,%s) '
        '   and asisug."preAsignacionCurso_id" = preasig.id '
        '   and pre."preProgramacion_id" = asisug."preProgramacion_id" '
        '   and pre."asignaturaXPrograma_id" = asi.id '
        '   and pre."preAsignacionCurso_id" = preasig.id '
        '   and pro.id = asi."programaAcademico_id" '
        '   and asig.id = asi."asignatura_id" '
        ' group by asisug."preAsignacionCurso_id",pro."sigla",asig."codigo" '
        ' ) a '
        ' group by a.corrida ',
        [corridaA, corridaB]
    )

    print('antes de fetchall ' + corridaA + ' ' + corridaB)
    cupos = cursor.fetchall()
    datosCupos = []
    for row in cupos:
        print('recorriendo cupos ', row[0])
        datosCupos.append(row[0])

    print('despues de recorrer cupos')
    p = {'ind':'%Cupos', 'a':str(datosCupos[0]),'b':str(datosCupos[1])}
    dataA.append(int(datosCupos[0]))
    dataB.append(int(datosCupos[1]))
    results.append(p)
    print('despues append')
    print(p)



    # Indicador 2: Satisfaccion
    cursor.execute(
        ' select round(avg(c.satisfaccion)) '
        ' ,c.corrida '
        ' from( '
        ' select (case when COALESCE(b.capacidad,0) >= 2 and COALESCE(a.asignadas,0)= 2 THEN 100 '
        ' when COALESCE(b.capacidad,0) >= 2 and COALESCE(a.asignadas,0)= 1 THEN 50 '
        ' when COALESCE(b.capacidad,0) >= 2 and COALESCE(a.asignadas,0)= 0 THEN 0 '
        ' when COALESCE(b.capacidad,0) >= 1 and COALESCE(a.asignadas,0)= 1 THEN 100 '
        ' when COALESCE(b.capacidad,0) >= 1 and COALESCE(a.asignadas,0)= 0 THEN 0 '
        ' else 0 end) satisfaccion '
        ' ,B.corrida '
        ' ,a.asignadas '
        ' ,b.capacidad '
        ' ,b.estudiante '
        ' from (select count(*) asignadas, asig.estudiante_id estudiante, asig."preAsignacionCurso_id" corrida '
        ' from siscupos_asignaturasugerida asig '
        ' where asig."preAsignacionCurso_id" IN (%s,%s) '
        ' group by asig.estudiante_id,asig."preAsignacionCurso_id" '
        ' order by 3,2 ) a '
        ' RIGHT OUTER JOIN  '
        ' (select count(*) capacidad, estudiante_id estudiante, asig."preAsignacionCurso_id" corrida '
        ' from siscupos_asignaturaxestudianteasig asig '
        ' where estado = \'0\'  '
        ' and asig."preAsignacionCurso_id" IN (%s,%s) '
        ' group by estudiante_id, asig."preAsignacionCurso_id" '
        ' order by 3,2) b '
        ' ON  b.estudiante = a.estudiante '
        ' AND b.corrida = a.corrida '
        ' order by 2,5 ) c '
        ' where c.corrida is not null '
        ' group by c.corrida ',
        [corridaA, corridaB, corridaA, corridaB]
    )
    print('2 antes de fetchall ' + corridaA + ' ' + corridaB)
    cupos = cursor.fetchall()
    datosSatis = []
    for row in cupos:
        print('recorriendo cupos ', row[0])
        datosSatis.append(row[0])

    print('2 despues de recorrer cupos')
    p = {'ind':'%Satisf.', 'a':str(datosSatis[0]),'b':str(datosSatis[1])}
    dataA.append(int(datosSatis[0]))
    dataB.append(int(datosSatis[1]))
    results.append(p)
    print('2 despues append')
    print(p)


    # Indicador 3: Asignacion de estudiantes
    cursor.execute(
       ' select round(avg(c.asignacion)) '
       '  ,c.corrida '
       '  from( '
       '  select (case when COALESCE(b.capacidad,0) >= 1 and COALESCE(a.asignadas,0)>= 1 THEN 100 '
       '  else 0 end) asignacion '
       '  ,b.corrida '
       '  ,a.asignadas '
       '  ,b.capacidad '
       '  ,b.estudiante '
       '  from (select count(*) asignadas, asig.estudiante_id estudiante, asig."preAsignacionCurso_id" corrida '
       '  from siscupos_asignaturasugerida asig '
       '  where asig."preAsignacionCurso_id" IN (%s,%s) '
       '  group by asig.estudiante_id,asig."preAsignacionCurso_id" '
       '  order by 2 ) a '
       '  RIGHT OUTER JOIN '
       '  (select count(*) capacidad, estudiante_id estudiante, asig."preAsignacionCurso_id" corrida '
       '  from siscupos_asignaturaxestudianteasig asig '
       '  where estado = \'0\'  '
       '  and asig."preAsignacionCurso_id" IN (%s,%s) '
       '  group by estudiante_id, asig."preAsignacionCurso_id" '
       '  order by 2) b '
       ' ON  b.estudiante = a.estudiante '
       '  AND b.corrida = a.corrida '
       '  order by 2,5) c   '
       '  group by c.corrida ',
        [corridaA, corridaB, corridaA, corridaB]
    )
    print('3 antes de fetchall ' + corridaA + ' ' + corridaB)
    cupos = cursor.fetchall()
    datosAsig = []
    for row in cupos:
        print('recorriendo cupos ', row[0])
        datosAsig.append(row[0])

    dataA.append(int(datosAsig[0]))
    dataB.append(int(datosAsig[1]))
    print('3 despues de recorrer cupos')
    p = {'ind':'%Estud.', 'a':str(datosAsig[0]),'b':str(datosAsig[1])}
    results.append(p)
    print('3 despues append')
    print(p)


    # Indicador 4: Atrasos por no poder tomar asignaturas
    cursor.execute(
            ' select 100-round(avg(c.asignacion)) atraso '
            ' ,c.corrida '
            ' from( '
            ' select (case when COALESCE(b.capacidad,0) >= 2 and COALESCE(a.asignadas,0)= 2 THEN 100 '
            ' when COALESCE(b.capacidad,0) = 1 and COALESCE(a.asignadas,0)= 1 THEN 100 '
            ' else 0 end) asignacion '
            ' ,b.corrida '
            ' ,a.asignadas '
            ' ,b.capacidad '
            ' ,b.estudiante '
            ' from (select count(*) asignadas, asig.estudiante_id estudiante, asig."preAsignacionCurso_id" corrida '
            ' from siscupos_asignaturasugerida asig '
            ' where asig."preAsignacionCurso_id" IN (%s,%s) '
            ' group by asig.estudiante_id,asig."preAsignacionCurso_id" '
            ' order by 2 ) a '
            ' RIGHT OUTER JOIN  '
            ' (select count(*) capacidad, estudiante_id estudiante, asig."preAsignacionCurso_id" corrida '
            ' from siscupos_asignaturaxestudianteasig asig '
            ' where estado = \'0\'  '
            ' and asig."preAsignacionCurso_id" IN (%s,%s) '
            ' group by estudiante_id, asig."preAsignacionCurso_id" '
            ' order by 2) b '
            ' ON  b.estudiante = a.estudiante '
            ' AND b.corrida = a.corrida '
            ' order by 2,5) c   '
            ' group by c.corrida ',
        [corridaA, corridaB, corridaA, corridaB]
    )
    print('4 antes de fetchall ' + corridaA + ' ' + corridaB)
    cupos = cursor.fetchall()
    datosRetraso = []
    for row in cupos:
        print('recorriendo cupos ', row[0])
        datosRetraso.append(row[0])

    dataA.append(int(datosRetraso[0]))
    dataB.append(int(datosRetraso[1]))
    print('4 despues de recorrer cupos')
    p = {'ind':'%Retraso', 'a':str(datosRetraso[0]),'b':str(datosRetraso[1])}
    results.append(p)
    print('4 despues append')
    print(p)


    # Indicador 5: Cumplimiento deseadas
    cursor.execute(
            ' select avg(d.peso), d.corrida '
            ' from( '
            ' select sum(c.pesoxmateria) peso, c.estudiante,c.corrida corrida '
            ' from (select a.asignatura_asig '
            ' ,b.asignatura_cap '
            ' ,b.estudiante estudiante '
            ' ,B.corrida_cap corrida '
            ' ,(case when COALESCE(a.asignatura_asig,0) = COALESCE(b.asignatura_cap,0) THEN 50 '
            ' else 0 end) pesoxmateria  '
            ' from (select asp.asignatura_id asignatura_asig, asig.estudiante_id estudiante, asig."preAsignacionCurso_id" corrida_asig '
            ' from siscupos_asignaturasugerida asig '
            ' ,siscupos_preProgramacion pre '
            ' ,siscupos_asignaturaxprograma asp '
            ' where asig."preProgramacion_id" = pre.id '
            ' and pre."asignaturaXPrograma_id" = asp.id '
            ' and asig."preAsignacionCurso_id" IN (%s,%s) '
            ' order by 2,1 ) a '
            ' RIGHT OUTER JOIN '
            ' (select asignatura_id asignatura_cap, estudiante_id estudiante, asig."preAsignacionCurso_id" corrida_cap '
            ' from siscupos_asignaturaxestudianteasig asig '
            ' where estado = \'3\'  '
            ' and asig."preAsignacionCurso_id" IN (%s,%s) '
            ' order by 2,1) b '
            ' ON  b.estudiante = a.estudiante '
            ' AND b.asignatura_cap = a.asignatura_asig '
            ' and b.corrida_cap = a.corrida_asig '
            ' order by 2,1) c '
            ' group by c.estudiante,c.corrida) d '
            ' group by d.corrida ',
        [corridaA, corridaB, corridaA, corridaB]
    )
    print('5 antes de fetchall ' + corridaA + ' ' + corridaB)
    cupos = cursor.fetchall()
    datosDeseo = []
    for row in cupos:
        print('recorriendo cupos ', row[0])
        datosDeseo.append(row[0])

    if len(datosDeseo) < 2:
        datosDeseo.append(0)
    if len(datosDeseo) < 2:
        datosDeseo.append(0)

    print('5 despues de recorrer cupos')
    p = {'ind':'%Deseo', 'a':str(datosDeseo[0]),'b':str(datosDeseo[1])}
    results.append(p)
    dataA.append(int(datosDeseo[0]))
    dataB.append(int(datosDeseo[1]))
    print('5 despues append')
    print(p)


    #Transformar a HighCharts
    resultsHC = []
    phcA ={'name':'Corrida '+str(corridaA), 'data':dataA}
    phcB ={'name':'Corrida '+str(corridaB), 'data':dataB}

    resultsHC.append(phcA)
    resultsHC.append(phcB)
    print(resultsHC)

    httpResp = HttpResponse(json.dumps(resultsHC), content_type='application/json; charset=UTF-8')

    print('antes de return')
    return httpResp
