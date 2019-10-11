from django.test import TestCase
from .models import Image,Location,Category

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.wecode= Category(name = 'food')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.wecode,Category))

    # Testing Save Method
    def test_save_method(self):
        self.wecode.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

