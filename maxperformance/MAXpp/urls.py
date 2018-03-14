from django.conf.urls import url
from . import views

app_name = 'MAXpp'
urlpatterns = [
    url(r'/auth/$', views.auth_view, name='auth'),
    url(r'/scores/$', views.scores_view, name='scores'),
    url(r'.com$', views.index, name='index'),
]
