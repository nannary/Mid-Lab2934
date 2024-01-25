from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('index',views.index),
    path('list',views.list),
    path('list', list, name='list'),
    path('login',views.custom_login),
    path('logout',views.logout_view),
]