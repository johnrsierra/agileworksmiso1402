from django.conf.urls import patterns, include, url

from siscupos import views
urlpatterns = patterns('',
    url(r'^$', views.index , name='index'),
    url(r'^programas/$',views.programas, name='programas'),
    url(r'^programas/demanda/$',views.demandaCupos, name='demanda'),
    url(r'^materias/$',views.materias, name='materias'),
    url(r'^estudiantes/$',views.estudiantes, name='estudiantes'),
)

