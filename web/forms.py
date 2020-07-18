from datetime import date

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from web.models import Reservation


class PastDateField(forms.DateTimeField):

    def validate(self, value):
        """Funkcja sprawdzająca czy wprowadzona data rezerwacji jest poprawna"""
        super().validate(value)
        if value <= timezone.now():
            raise ValidationError('Wybrany przez ciebie termin jest nie poprawny!')


class ReservationForm(forms.ModelForm):
    reservation_date = PastDateField(input_formats=['%d/%m/%Y %H:%M'], label='Termin sesji',
                                     help_text='(Format: dd/mm/yyyy HH:MM)')

    class Meta:
        model = Reservation
        fields = ['user', 'first_name', 'last_name', 'session_type', 'reservation_date']
        labels = {'first_name': 'Imię', 'last_name': 'Nazwisko', 'session_type': 'Typ sesji', 'user': 'Użytkownik'}
