from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import ListView
from .models import UserFilesUpload



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto {username} zostało utworzone poprawnie')
            return redirect('login')
        else:
            messages.error(request, 'Konto nie zostało utworzone')
            return render(request, 'registration/registration.html', {'form': form})
    else:
        form = UserRegisterForm()

    return render(request, 'registration/registration.html', {'form': form})


# def view_profile(request):
#     args = {'user': request.user}
#     return render(request, 'profile.html')


def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Konto zostało zaktualizowane!')
            return redirect('download')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Hasło zostało zmienione!')
            return redirect('download')
        else:
            messages.error(request, 'Hasło nie zostało zmienione!')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'change_password.html', args)


class DownloadView(ListView):
    model = UserFilesUpload
    context_object_name = 'down'
    fields = ['file']
    template_name = 'profile.html'

    def get_queryset(self):
        return UserFilesUpload.objects.filter(owner=self.request.user)