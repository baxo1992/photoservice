from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from users.forms import (
    SubmittableAuthenticationForm,
    SubmitablePasswordChangeForm
)


# Create your views here.
class SubmittableLoginView(LoginView):
    form_class = SubmittableAuthenticationForm
    template_name = 'form.html'


class SubmittablePasswordChangeView(PasswordChangeView):
    form_class = SubmitablePasswordChangeForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'templates/registration/registration.html', args)
