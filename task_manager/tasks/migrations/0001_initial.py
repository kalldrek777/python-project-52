# Generated by Django 5.0.1 on 2024-01-27 14:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('statuses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(max_length=1048576)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='executor', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='status', to='statuses.status')),
            ],
        ),
    ]
