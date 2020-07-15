from django.urls import path

from .views import (
    register,
    DownloadView,
    view_profile,
    edit_profile,
    change_password
)


urlpatterns = [
    path('register/', register, name='register'),
    path('download/', DownloadView.as_view(), name='download_list'),
    path('profile/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/change-password', change_password, name='change_password')
]
