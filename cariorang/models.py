from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.text import Truncator
from django.utils.html import mark_safe
from markdown import markdown

# Create your models here.

class PostCari(models.Model):
    name = models.CharField(max_length= 100, blank = True)
    umur = models.PositiveIntegerField(blank = True)
    tinggi = models.PositiveIntegerField(blank = True , null= True)
    berat  = models.PositiveIntegerField(blank = True , null=True)
    reward = models.DecimalField(max_digits = 1000, decimal_places = 2)
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User,related_name="cariorang",on_delete=models.CASCADE)
    lokasi_hilang = models.CharField(max_length=100, blank = True , null = True)
    picture = models.ImageField( upload_to = 'picture/', null =True , blank = True)
    desc = models.TextField(max_length = 5000)
    gender = (('Laki-Laki','Laki-Laki'),('Perempuan','Perempuan'))
    gender = models.CharField(max_length = 10, choices = gender , default="gender")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+62'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    approved_post = models.BooleanField(default = False)
    message_admin = models.TextField(max_length=1000 , default="", blank =True)
    ketemu = models.BooleanField(default = False)

    def approve(self):
        self.approved_post = True
        self.save()

    def ketemu_approve(self):
        self.ketemu = True
        self.save()

    def __str__(self):
        return self.name


class Detail(models.Model):
    postcari = models.ForeignKey(PostCari, related_name="details", on_delete=models.CASCADE)
    message = models.TextField(max_length= 5000 , default="")
    created_at = models.DateTimeField(auto_now_add = True )
    created_by = models.ForeignKey(User,related_name="details",on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null = True)
    update_by = models.ForeignKey(User, null=True, related_name="+",on_delete=models.CASCADE)

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(10)

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))
