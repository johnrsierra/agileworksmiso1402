from django.conf.urls import patterns, include, url

from siscupos import views
urlpatterns = patterns('',
    url(r'^$', views.index , name='index'),

)

