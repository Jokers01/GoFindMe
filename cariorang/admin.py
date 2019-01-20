from django.contrib import admin
from .models import PostCari , Detail



#customize field in admin site
admin.site.site_title = "CariOrang Admin"
admin.site.site_header = "CariOrang Admin"
admin.site.index_title = "Selamat Datang Admin"

# Register your models here.

admin.site.register(PostCari)
admin.site.register(Detail)
