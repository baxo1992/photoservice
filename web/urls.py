from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('SesjaS/', views.sessionW, name='sessionW'),
    path('SesjaR/', views.sessionF, name='sessionF'),
    path('SesjaC/', views.sessionP, name='sessionP'),
    path('about/', views.about, name='about'),
    path('photos/', views.PhotoView.as_view(), name='photo'),
    path('reservation/', views.ReservationView.as_view(), name='reservation'),
    path('reservation-succes/', views.reservation_succes, name='reservation-succes'),
]
