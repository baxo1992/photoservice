from django.db import models
from django.utils import timezone
from users.models import Profile
from django.contrib.auth.models import User


# Create your models here.


class Session(models.Model):
    # tabela(model) z wszystkimi typami sesji fotograficznych
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    # Tabela (model) z wszystkimi rezerwacjami, połączona z konkretnym użytkownikiem oraz konkretnym typem sesji
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=32, null=True, blank=False)
    last_name = models.CharField(max_length=32, null=True, blank=False)
    session_type = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
    reservation_date = models.DateTimeField()

    def __str__(self):
        return f"{self.reservation_date} - {self.first_name} {self.last_name} / {self.session_type}"


class News(models.Model):
    # Tabela (model) z wszystkimi newsami
    title = models.CharField(max_length=40)
    body = models.TextField(null=False, blank=False)
    publication_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


def pic_path(instance, filename):
    return 'User_Photos/{0}/{1}/'.format(instance.reservation, filename)


class Photos(models.Model):
    # Tabela (model) z wszystkimi zdjęciami, połączona z tabelą Reservation
    reservation = models.ForeignKey(Reservation, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    img = models.ImageField(upload_to=pic_path, blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.reservation)
