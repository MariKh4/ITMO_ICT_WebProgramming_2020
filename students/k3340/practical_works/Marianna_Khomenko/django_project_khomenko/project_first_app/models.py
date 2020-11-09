from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField(blank=True, null=True)

    PassportID = models.CharField(max_length=30, blank=True, null=True)
    HomeAddress = models.CharField(max_length=100, blank=True, null=True)
    Nationality = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

User = get_user_model()

class DriversLicense(models.Model):
    carowner = models.ForeignKey(User, on_delete=models.CASCADE)
    TYPE_DL = [
        ('A','A'),('A1','A1'),
        ('B','B'),('B1','B1'),
        ('C','C'),('C1','C1'),
        ('D','D'),('D1','D1'),
        ('BE','BE'),('CE','CE'),
        ('C1E','C1E'),('DE','DE'),
        ('D1E','D1E'),('M','M'),
        ('Tm','Tm'),('Tb','Tb')
        ]
    number = models.IntegerField()
    date_i = models.DateField()
    type_l = models.CharField(max_length= 3, choices = TYPE_DL)

class Car(models.Model):
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    state_number = models.CharField(max_length=50)

class Possession(models.Model):
    carowner = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_s = models.DateField()
    date_e = models.DateField()


class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()

    def __str__(self):
        return self.title
        




