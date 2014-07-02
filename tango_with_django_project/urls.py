from django.conf.urls import patterns, include, url
from rango import views
from rango.urls import urlpatterns as rango_urls
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^rango/', include(rango_urls)),
    url(r'^admin/', include(admin.site.urls)),
)
