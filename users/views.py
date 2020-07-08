from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy

from users.forms import (
    SubmittableAuthenticationForm,
    SubmitablePasswordChangeForm
)


# Create your views here.
class SubmittableLoginView(LoginView):
    form_class = SubmittableAuthenticationForm
    template_name = 'registration/login.html'


class SubmittablePasswordChangeView(PasswordChangeView):
    form_class = SubmitablePasswordChangeForm
    template_name = 'form.html'
    success_url = reverse_lazy('home')
