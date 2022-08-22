from datetime import date, datetime
from xmlrpc.client import DateTime
from django.db import models

# Create your models here.
class chatRoom(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    message = models.CharField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.message