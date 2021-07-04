from django.test import TestCase
from .models import Image,Categories,Image_Location
import datetime as dt

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new tag and saving it

        self.new_categories = Categories(name = 'testing')
        self.new_category.save()

        self.new_image= Image(title = 'Test Image',post = 'This is a random test Post')
        self.new_image.save()

        self.new_image.categories.add(self.new_categories)
    def tearDown(self):
        Categories.objects.all().delete()
        Image.objects.all().delete()

# Location tests
class Location(TestCase):
    def setUp(self):
        self.new_location = Location(name='Nairobi')

    def test_category_instance(self):
        self.assertTrue(isinstance(self.new_location, Location))

    def save_location(self):
        before = Location.objects.count()
        self.new_location.save_location()
        after = Location.objects.count()
        self.assertTrue(before < after)

    def tearDown(self):
        Location.objects.all().delete()

# Testing image class
class TestImage(TestCase):
    def setUp(self):
        self.category = Categories(name='iconic')
        self.category.save()

        self.location = Location(place='juja')
        self.location.save_location()

        self.new_image = Image(name='happy', description='A happy girl', category=self.category, location=self.location,upload_date= dt.date.today(), url='./image/happy.png')

    def test_image_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))


    def test_image_id(self):
        pass

    def test_search_image(self):
        pass

    def test_save_image(self):
        before = Image.objects.count()
        self.new_image.save_image()
        after = Image.objects.count()
        self.assertTrue(before < after)

    def test_search_by_title(self):
        pass

    def tearDown(self):
        Image.objects.all().delete()


    
