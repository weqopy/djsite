from django.conf.urls import url
from . import views as main_views

app_name = 'main'
urlpatterns = [
    url(r'^$', main_views.index, name='index'),
]
