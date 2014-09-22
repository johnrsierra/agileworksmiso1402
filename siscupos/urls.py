from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from siscupos import views
urlpatterns = patterns('',
    url(r'^$', views.index , name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^coordinacion/$',views.coordinacion, name='coordinacion'),
    url(r'^coordinacion/demanda/$',views.demandaCupos, name='demanda'),
    url(r'^coordinacion/optimizador/$',views.ejecuciones, name='optimizador'),
    url(r'^coordinacion/optimizador/(?P<preasig_id>\w+)/resultados/$',views.resultado,name='resultado'),
    url(r'^materias/$',views.materias, name='materias'),
    url(r'^estudiantes/$',views.estudiantes, name='estudiantes'),
    url(r'^coordinacion/asignatura/$',views.jsonTest,name='asignatura'),
)

