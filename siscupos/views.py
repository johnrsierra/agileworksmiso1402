from django.shortcuts import render
from siscupos.models import Asignatura,AsignaturaSugerida,AsignaturaXEstudiante,AsignaturaXPrograma,Estudiante,PreAsignacionCurso,PreProgramacion,ProgramaAcademico
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Count

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

#Lista los cursos que han sido seleccionados por los estudiantes y aun no han sido cursados
#Cursados -> 0 no ha sido cursado
#            1 ya fue cursado
def demandaCupos(request):
    lista_demanda = Asignatura.objects.annotate(demanda=Count('asignaturaxestudiante')).filter(asignaturaxestudiante__cursada='0')
    print lista_demanda[0]
    context = {'lista_demanda':lista_demanda}
    return render(request,'programas/demanda.html',context)
