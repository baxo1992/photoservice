from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import News, Session
from .forms import ReservationForm


# Widok dla strony Głównej
def home(request):
    posts = News.objects.all()
    return render(request, 'home.html', {'posts': posts, 'title': 'Photo Service'})


# Widok Sesja Ślubna
def sessionW(request):
    return render(request, 'sessionW.html', {'title': 'Sesja Ślubna'})


# Widok Sesja Rodzinna
def sessionF(request):
    return render(request, 'sessionF.html', {'title': 'Sesja Rodzinna'})


# Widok Sesja Ciążowa
def sessionP(request):
    return render(request, 'sessionP.html', {'title': 'Sesja Ciążowa'})


# Widok O mnie
def about(request):
    return render(request, 'about.html', {'title': 'O mnie'})


# Widok Rezerwacja
def reservation(request):
    return render(request, 'reservation.html', {'title': 'Rezerwacja'})


class ReservationView(CreateView):
    title = 'Rezerwacja'
    template_name = 'reservation.html'
    form_class = ReservationForm
    success_url = reverse_lazy('reservation-succes')

# Widok Pomyślnej rezerwacjii
def reservation_succes(request):
    return render(request, 'reservation-succes.html', {'title': 'Rezerwacja'})