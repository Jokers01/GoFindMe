# Generated by Django 2.0.5 on 2018-09-17 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cariorang', '0012_auto_20180915_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcari',
            name='message_admin',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
