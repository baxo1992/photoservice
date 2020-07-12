from django.urls import path
from .views import register, DownloadView
from . import views


urlpatterns = [
    path('register/', register, name='register'),
    path('download/', DownloadView.as_view(), name='download_list'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change-password', views.change_password, name='change_password')
]