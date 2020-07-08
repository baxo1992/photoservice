from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    email = models.EmailField()

    phone_regex = RegexValidator(regex=r'^\d{9,15}$', message='Numer telefonu powinnien posiadać od 9 do 15 cyfr!')

    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
