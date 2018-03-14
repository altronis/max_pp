from django.conf.urls import url
from . import views

app_name = 'MAXpp'
urlpatterns = [
    url(r'^MAXpp/$', views.index, name='index'),
    url(r'^MAXpp/auth/$', views.auth_view, name='auth'),
    url(r'^MAXpp/scores/$', views.scores_view, name='scores'),
]
