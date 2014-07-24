from django.conf.urls import patterns, include, url
from rango import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ##url(r'^rango/', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^add_category/', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
    url(r'^category/(?P<category_name_url>\w+)/add_page/', views.add_page, name='category'),
    ##url(r'^rango/', 'rango.views.index'),
    #url(r'^admin/', include(admin.site.urls)),
)
