from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .forms import UserRegisterForm
from users.forms import (
    SubmittableAuthenticationForm,
    SubmitablePasswordChangeForm,
    EditProfileForm
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
    success_message = 'Hasło zostało zmienione poprawnie!'


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

    return render(request, 'registration/registration.html', {'form': form})


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html')


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('view_profile')
        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'change_password.html', args)