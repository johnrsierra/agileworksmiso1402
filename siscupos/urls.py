from django.conf.urls import patterns, include, url

from siscupos import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index , name='index'),
    url(r'^siscupos/',include('siscupos.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)

