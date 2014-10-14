from django.conf.urls import patterns, url

from pypi import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^submit$', views.submit, name='submit'),
    url(r'^thankyou/(?P<emailid>\d+?)/$', views.thankyou, name='thankyou'),
)
