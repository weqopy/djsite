from django.conf.urls import url
from . import views as polls_views


app_name = 'polls'
urlpatterns = [
    url(r'^$', polls_views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', polls_views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', polls_views.results,
        name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', polls_views.vote, name='vote'),

]
