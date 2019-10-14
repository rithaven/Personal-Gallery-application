from django.test import TestCase
from .models import Image,Location,Category

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.wecode= Image(name = 'food'description ='akako ni keza pe')
        self.wecode.save_image()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.wecode,Image))
    # Testing Save Method
    def test_save_method(self):
        self.wecode.save_Image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self

