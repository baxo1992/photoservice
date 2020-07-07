from django.urls import path
from django.contrib.auth.views import LogoutView

from users.views import SubmittableLoginView


urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]