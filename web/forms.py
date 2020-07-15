from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from web.models import Reservation


def past_date_field(value):
    if value.date <= date.today():
        raise ValidationError('Błędna data')


class ReservationForm(forms.ModelForm):
    reservation_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], label='Termin sesji', help_text='(Format: dd/mm/yyyy HH:MM)')

    class Meta:
        model = Reservation
        fields = ['user', 'first_name', 'last_name', 'session_type', 'reservation_date']
        # fields = ['session_type', 'reservation_date']
        labels = {'first_name': 'Imię', 'last_name': 'Nazwisko', 'session_type': 'Typ sesji', 'user': 'Użytkownik'}
