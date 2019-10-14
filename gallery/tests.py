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
        self.new_image=Image(name='umugeni', description='the beautifull wedding')
        self.new_image.save_image()
        self.new_image.delete_image()
        images=Image.objects.all()
        self.assertEqual(len(images),1)

    def test_update_method(self):
        self.pic=Image(name ='fa',description='ifoto ya fa')
        self.pic.save_image()
        self.pic=Image(name'KAKA',description='ntugasibe')
        self.pic.update_image(name='KAKA')
        self.pic.save_image()
        images=Image.objects.filter(name='danvic')
        photos=Image.objects.all()
        self.assertEqual(len(images),1)

class

    

