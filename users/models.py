from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, default='')
    second_name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.first_name + ' ' + self.last_name