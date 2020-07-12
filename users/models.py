from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse


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


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


def pic_path(instance, filename):
    return 'User_files/{0}/{1}/{2}/{3}'.format(instance.owner, instance.session_type, instance.upload_date, filename)


class UserFilesUpload(models.Model):

    SESSION_TYPES = (
        ('sesja ślubna', 'Sesja Ślubna'),
        ('sesja rodzinna', 'Sesja Rodzinna'),
        ('sesja ciążowa', 'Sesja Ciążowa'),
    )

    uploaded_by = models.CharField(default='admin', max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    session_type = models.CharField(max_length=30, choices=SESSION_TYPES, default='sesja ślubna')
    file = models.FileField(upload_to=pic_path, blank=True, null=True)
    upload_date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.owner)

    def get_absolute_url(self):
        return reverse('download_list', kwargs={'pk': self.pk})