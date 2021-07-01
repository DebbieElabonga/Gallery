import images
from django.db import models
import datetime as dt

# Create your models here.
class Image_Location (models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Categories(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    @classmethod
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    
class Image(models.Model):
    image = models.ImageField(upload_to = 'image/')
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Image_Location,on_delete=models.CASCADE)
    categories= models.ForeignKey(Categories,on_delete=models.CASCADE)

    def __str__(self):
        return self.image
    
    def save_image (self):
        self.save
        

    def delete_image (self):
        self.save

    @classmethod
    def get_image_by_id(cls, image_id):
        image = Image.objects.get(id=image_id)
        return image

    @classmethod
    def search_by_category(cls, categories):
        images = cls.objects.filter(categories__name__icontains=categories).all()
        return Image

    @classmethod
    def filter_by_location(cls, location):
        Image_Location = Image.objects.filter(location__name=location).all()
        return  images






