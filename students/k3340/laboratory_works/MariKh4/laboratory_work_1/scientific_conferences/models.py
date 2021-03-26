from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Location(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.address)


class Conference(models.Model):
    title = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.title)

class Speaker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name, self.position)


class Speech(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)


class Comment(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True)
    data = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('data',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user.first_name, self.conference)