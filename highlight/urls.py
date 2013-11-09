from django.conf.urls import patterns, url

from highlight import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
