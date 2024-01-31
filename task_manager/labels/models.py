from django.db import models


# Create your models here.
class Label(models.Model):
    name = models.CharField(
        max_length=100, unique=True
    )
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def is_object_in_use(self):
        return True if self.task_set.exists() else False
