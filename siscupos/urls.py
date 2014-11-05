from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from siscupos import views
urlpatterns = patterns('',
    url(r'^$', views.index , name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^coordinacion/$',views.coordinacion, name='coordinacion'),
    url(r'^coordinacion/demanda/$',views.demandaCupos, name='demanda'),
    url(r'^coordinacion/optimizador/asignacionr/(?P<prog>\w+)/(?P<corrida>\w+)/$',views.consultarAsignacionPrograma, name='asignacionr'),#retorna el resultado del optimizador por plan
    url(r'^coordinacion/optimizador/asignacions/(?P<corrida>\w+)/$',views.consultarSatisfaccionPrograma, name='asignacions'),#retorna el resultado de satisfaccion
    url(r'^coordinacion/optimizador/demanda/(?P<corrida>\w+)/$',views.demandaxasignacion, name='demanda'),#retorna la demanda vs la asignacion de la corrida
    url(r'^coordinacion/optimizador/indicadores/(?P<corridaA>\w+)/(?P<corridaB>\w+)/$',views.indicadores, name='indicadores'),#retorna los indicadores de la corrida
    url(r'^coordinacion/optimizador/indicadoresDetalleSatis/(?P<corrida>\w+)/$',views.indicadoresDetalleSatis, name='indicadoresDetalleSatis'),#retorna los indicadores de la corrida
    url(r'^coordinacion/optimizador/indicadoresDetalleCupos/(?P<corrida>\w+)/$',views.indicadoresDetalleCupos, name='indicadoresDetalleCupos'),#retorna los indicadores de la corrida
    url(r'^coordinacion/optimizador/indicadoresDetalleEstudiantes/(?P<corrida>\w+)/(?P<porc_satisfaccion>\w+)/$',views.indicadoresDetalleEstudiantes, name='indicadoresDetalleEstudiantes'),#retorna los indicadores de la corrida
    url(r'^coordinacion/optimizador/$',views.ejecuciones, name='optimizador'),
    url(r'^coordinacion/optimizando/$',views.optimizando, name='optimizando'),
    url(r'^coordinacion/optimizador/(?P<preasig_id>\w+)/resultados/$',views.resultado,name='resultado'),
    url(r'^coordinacion/programacion/(?P<prog_id>\w+)/plan/$',views.consultarPreProgramacion,name='plan'),
    url(r'^coordinacion/asignatura/$',views.jsonTest,name='asignatura'),
    url(r'^materias/$',views.materias, name='materias'),
    url(r'^estudiantes/$',views.estudiantes, name='estudiantes'),
    url(r'^estudiantes/(?P<est_id>\w+)/carpeta/$',views.carpeta,name='carpeta'),
    url(r'^estudiante/(?P<est_id>\w+)/carpetaestudiante/$',views.micarpeta,name='carpetaestudiante'),
    url(r'^estudiante/(?P<est_id>\w+)/nuevacarpeta/$',views.nuevacarpeta,name='nuevacarpeta'),
)

