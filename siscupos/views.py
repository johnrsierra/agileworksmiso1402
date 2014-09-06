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
    return render(request,'index.html', {})
