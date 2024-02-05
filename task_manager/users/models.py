from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_full_name(self):
        return self.__str__()

    def get_author_username(self):
        return self.username
