from django.conf.urls import url
from . import views

app_name = 'MAXpp'
urlpatterns = [
    url(r'^MAXpp/$', views.index, name='index'),
    url(r'^MAXpp/signup/$', views.signup_view, name='signup'),
    url(r'^MAXpp/signup/auth/$', views.signup_auth, name='signup_auth'),
    url(r'^MAXpp/login/$', views.login_view, name='login'),
    url(r'^MAXpp/login/auth/$', views.auth_view, name='auth'),
    url(r'^MAXpp/logout/$', views.logout_view, name='logout'),
    url(r'^MAXpp/scores/$', views.scores_view, name='scores'),
    url(r'^MAXpp/scores/add/$', views.scores_add, name='scores_add'),
]
