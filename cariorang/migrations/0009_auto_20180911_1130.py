# Generated by Django 2.0.5 on 2018-09-11 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cariorang', '0008_auto_20180911_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='postcari',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='cariorang.PostCari'),
        ),
    ]
