from django.conf.urls import patterns, url 

from glopss_app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
#       url(r'^p1_submit/$', views.p1_submit, name='index'),
#        url(r'^mcqhome$', views.mcqhome, name='mcqhome'),

)

