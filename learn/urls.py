from django.conf.urls import url
from . import views as learn_views


app_name = 'learn'
urlpatterns = [
    # views.index
    url(r'^$', learn_views.index, name='index'),
    url(r'^temp/$', learn_views.temp, name='temp'),
    url(r'^add_form/$', learn_views.add_form, name='add_form'),
    url(r'^add/$', learn_views.add, name='add'),
    url(r'^add/(\d+)/(\d+)/$', learn_views.old_url_redirect),
    url(r'^new_add/(\d+)/(\d+)/$', learn_views.add2, name='add2'),
]
