from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from rango import views
from rango.urls import urlpatterns as rango_urls



admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'), #should change this to a proper index page to avoid /rango/rango url issue
    url(r'^rango/', include(rango_urls)),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )