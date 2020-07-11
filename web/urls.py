from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('SesjaS/', views.sessionW, name='sessionW'),
    path('SesjaR/', views.sessionF, name='sessionF'),
    path('SesjaC/', views.sessionP, name='sessionP'),
    path('about/', views.about, name='about'),
    path('reservation/', views.reservation, name='reservation'),
]