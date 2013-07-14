from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

from glopss_app import views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),


	url(r'^glopss/', include('glopss_app.urls', namespace="glopss")),


    # Examples:
    # url(r'^$', 'glopss.views.home', name='home'),
    # url(r'^glopss/', include('glopss.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
