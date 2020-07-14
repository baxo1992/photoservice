from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Row, Submit, Layout

from users.models import Profile
from web.models import Reservation
from django.contrib.admin import widgets

from datetime import date


def past_date_field(value):
    if value.date <= date.today():
        raise ValidationError('Błędna data')


class ReservationForm(forms.ModelForm):
    reservation_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], label='Termin sesji', help_text='(Format: dd/mm/yyyy HH:MM)')

    class Meta:
        model = Reservation
        fields = '__all__'
        # fields = ['session_type', 'reservation_date']
        labels = {'session_type': 'Typ sesji', 'user': 'Użytkownik'}
