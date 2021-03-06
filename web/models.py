from django.db import models
from django.utils import timezone
from users.models import Profile


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
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    session_type = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
    reservation_date = models.DateTimeField()

    def __str__(self):
        return f"{self.reservation_date.day}/{self.reservation_date.hour} - {self.user.first_name} {self.user.last_name}"


class News(models.Model):
    # Tabela (model) z wszystkimi newsami
    title = models.CharField(max_length=40)
    body = models.TextField(null=False, blank=False)
    publication_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Photos(models.Model):
    # Tabela (model) z wszystkimi zdjęciami, połączona z tabelą Reservation
    reservation = models.ForeignKey(Reservation, on_delete=models.DO_NOTHING)
    description = models.TextField()
    file = models.FileField(upload_to='photos/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reservation
