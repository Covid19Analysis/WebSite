from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.
# user = settings.AUTH_USER_MODEL


class girdi(models.Model):
    tarih = models.DateField()
    bugunkuVaka = models.PositiveIntegerField()
    bugunkuHasta = models.PositiveIntegerField()
    bugunkuTest = models.PositiveIntegerField()
    bugunkuVefat = models.PositiveIntegerField()
    bugunkuIyilesen = models.PositiveIntegerField()
    agirHasta = models.PositiveIntegerField()

    def __str__(self):
        return str(self.tarih) + " tarihli girdiler"


    # for i in User.objects.all():
    #     if i:
    #         print(i.id, i.username, i.is_authenticated)
    # kullanici = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class ozelGunler(models.Model):
    tarih = models.DateField()
    ozelGunTuru = CharField(max_length=200)
    aciklama = CharField(max_length=500)

    def __str__(self):
        return str(self.tarih) + " tarihli özel gün"


# class user(models.Model):
#     userName = models.CharField()

# hastalardaZaturreOrani,
# toplamTest,
# toplamVaka,
# toplamVefat,
# toplamIyilesenHasta,
