from django.shortcuts import render
from .models import Image_Location, Image, Categories

# Create your views here.
def welcome(request):
    images = Image.all_images()
    return render(request, 'all-images.html',{'images': images})
