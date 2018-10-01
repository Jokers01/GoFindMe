# Generated by Django 2.0.5 on 2018-09-15 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cariorang', '0011_postcari_approved_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detail',
            name='created_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='details', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
