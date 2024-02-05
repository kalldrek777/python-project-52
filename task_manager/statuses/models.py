from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def is_object_in_use(self):
        return True if self.status.exists() else False
