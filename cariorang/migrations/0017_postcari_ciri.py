# Generated by Django 2.0.5 on 2018-10-31 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cariorang', '0016_auto_20181003_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcari',
            name='ciri',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]