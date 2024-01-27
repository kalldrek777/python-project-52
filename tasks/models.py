from django.db import models
from users.models import CustomUser
from statuses.models import Status
from labels.models import Label


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1048576)
    created_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        related_name='author'
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='status'
    )
    executor = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        related_name='executor'
    )
    labels = models.ManyToManyField(Label, blank=True)