from django.conf.urls import patterns, url

from EdgeCalApp import views

urlpatterns = patterns('EdgeCalApp.views',
    # ex: /EdgeCalApp/
    url(r'^$', views.index, name='index'),
    # ex: /EdgeCalApp/5/
    url(r'^(?P<user_id>\d+)/$', views.detail, name='detail'),
    # ex: /EdgeCalApp/5/results/
    url(r'^(?P<user_id>\d+)/results/$', views.results, name='results'),
    # ex: /EdgeCalApp/5/vote/
    url(r'^(?P<user_id>\d+)/vote/$', views.vote, name='vote'),
)