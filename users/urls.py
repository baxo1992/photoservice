from django.urls import path
from django.contrib.auth.views import LogoutView

from users.views import SubmittableLoginView, register
from users import views


urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change-password', views.change_password, name='change_password')
]