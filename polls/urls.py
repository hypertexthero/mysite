from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # index page
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    # detail page
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    
    # results page
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    
    # vote ation
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)