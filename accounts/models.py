from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = (
    ('Banda Aceh','Banda Aceh'),('Medan','Medan'),('Padang','Padang'),('Jambi','Jambi'),('Palembang','Palembang'),('Pangkal Pinang','Pangkal Pinang'),
    ('Bengkulu','Bengkulu'),('Bandar Lampung','Bandar Lampung'),('Jakarta','Jakarta'),('Bandung','Bandung'),
    ('Serang','Serang'),('Semarang','Semarang'),('Yogyakarta', 'Yogyakarta'),('Surabaya','Surabaya'),('Denpasar','Denpasar'),
    ('Mataram', 'Mataram'),('Kota Mamuju','Kota Mamuju'),('Palu','Palu'),('Kendari','Kendari'),('Makasar','Makasar'),('Gorontalo','Gorontalo'),
    ('Ambon','Ambon'),('Ternate','Ternate'),('Kota Manokwari','Kota Manokwari'),('Jayapura','Jayapura'))
    location = models.CharField(max_length=100, blank=True)
    gender = (
    ('Laki-Laki','Laki-Laki'),
    ('Perempuan','Perempuan')
    )
    gender = models.CharField(max_length = 10, choices = gender , default="gender")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+62'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, default="")
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    users = User.objects.filter(profile=None)
    for user in users:
        Profile.objects.create(user=user)
    instance.profile.save()
