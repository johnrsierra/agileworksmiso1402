from django.shortcuts import render,HttpResponse
from siscupos.models import Asignatura,AsignaturaSugerida,AsignaturaXEstudiante,AsignaturaXPrograma,Estudiante,PreAsignacionCurso,PreProgramacion,ProgramaAcademico
from django.shortcuts import render_to_response
from django.template import RequestContext

import json
from django.core import serializers

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

def materias(request):
    lista_materias = Asignatura.objects.all()
    context = {'lista_materias':lista_materias}
    return render(request,'materias/lista_materias.html',context)

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
    lista_ejecuciones = PreAsignacionCurso.objects.all()
    context = {'lista_ejecuciones':lista_ejecuciones}
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
    data = serializers.serialize('json', asig, fields=('name','size'))
    return HttpResponse(data, content_type='application/json; charset=UTF-8')