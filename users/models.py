from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()

    phone_regex = RegexValidator(regex=r'^\d{9,15}$', message='Numer telefonu powinnien posiadać od 9 do 15 cyfr!')

    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
