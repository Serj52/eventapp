from django.db import models
import datetime
# Create your models here.


class Events(models.Model):
    name = models.TextField(null=False)
    created = models.DateField(null=False, default=datetime.date.today)
    status = models.CharField(max_length=20, default='создан', null=False)
    folder = models.TextField(null=False)
class Organizer(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=20, null=False)
    surname = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
class Deadline(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, null=False)
    date = models.DateField(null=False)
