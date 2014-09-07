from django.shortcuts import render
from siscupos.models import Asignatura,AsignaturaSugerida,AsignaturaXEstudiante,AsignaturaXPrograma,Estudiante,PreAsignacionCurso,PreProgramacion,ProgramaAcademico
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q

# Create your views here.
def index(request):
    contactos = 1
    grupos = 1
    ubicaciones = 1
    context = {'nuevos_contactos':contactos,'nuevos_grupos':grupos,'nuevas_ubicaciones':ubicaciones}
    return render(request,'index.html', context)

def programas(request):
    lista_programas = ProgramaAcademico.objects.all()
    context = {'lista_programas':lista_programas}
    return render(request,'programas/lista_programas.html',context)

def materias(request):
    lista_materias = Asignatura.objects.all()
    context = {'lista_materias':lista_materias}
    return render(request,'materias/lista_materias.html',context)

def estudiantes(request):
    lista_estudiantes = Estudiante.objects.all()
    context = {'lista_estudiantes':lista_estudiantes}
    return render(request,'estudiantes/lista_estudiantes.html',context)

def demandaCupos(request):
    lista_preprogramacion = PreProgramacion.objects.all()
    context = {'lista_preprogramacion':lista_preprogramacion}
    return render(request,'programas/demanda.html',context)
