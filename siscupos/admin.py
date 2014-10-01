from django.contrib import admin
from siscupos.models import Asignatura,Estudiante,ProgramaAcademico,AsignaturaXEstudiante,PreProgramacion,AsignaturaXPrograma

admin.site.register(Asignatura)
admin.site.register(Estudiante)
admin.site.register(ProgramaAcademico)
admin.site.register(AsignaturaXEstudiante)
admin.site.register(AsignaturaXPrograma)
admin.site.register(PreProgramacion)