from django.contrib import admin
from django.contrib import admin
from .models import Image, Categories, Image_Location

# Register your models here.
admin.site.register(Image)
admin.site.register(Categories)
admin.site.register(Image_Location)