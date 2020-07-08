from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm
from users.forms import (
    SubmittableAuthenticationForm,
    SubmitablePasswordChangeForm
)


# Create your views here.
class SubmittableLoginView(SuccessMessageMixin, LoginView):
    form_class = SubmittableAuthenticationForm
    template_name = 'registration/login.html'
    success_message = 'Zostałeś zalogowany poprawnie!'


class SubmittablePasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = SubmitablePasswordChangeForm
    template_name = 'form.html'
    success_url = reverse_lazy('home')
    success_message = 'Hasło zostało zmienione poprawnie !'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto {username} zostało utworzone poprawnie')
            return redirect('login')
    else:
        form = UserRegisterForm()
        messages.error(request, 'Konto niezostało utworzone')
    return render(request, 'registration/registration.html', {'form': form})
