from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import *
from django.db.models.signals import post_save
from django.dispatch import receiver

class Management(models.Model):
    Work_name = models.CharField(max_length=200)
    Description = models.TextField(default='-', blank=True)

    def __str__(self):
        return self.Work_name