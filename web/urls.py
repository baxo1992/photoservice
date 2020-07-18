from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sessionW/', views.sessionW, name='sessionW'),
    path('sessionF/', views.sessionF, name='sessionF'),
    path('sessionP/', views.sessionP, name='sessionP'),
    path('about/', views.about, name='about'),
    path('photos/', views.PhotoView.as_view(), name='photo'),
    path('reservation/', views.ReservationView.as_view(), name='reservation'),
]
