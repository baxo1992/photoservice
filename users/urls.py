from django.urls import path
from users.views import register
from users import views


urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change-password', views.change_password, name='change_password')
]