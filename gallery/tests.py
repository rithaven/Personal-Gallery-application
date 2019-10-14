from django.test import TestCase
from .models import Image,Location,Category

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.wecode= Image(name = 'food',description ='akako ni keza pe')
        self.wecode.save_image()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.wecode,Image))
    # Testing Save Method
    def test_save_method(self):
        self.wecode.save_Image()
        myphoto = Image.objects.all()
        self.assertTrue(len(myphoto) > 0)

    def test_delete_method(self):
        self.new_image=Image(name='umugeni', description='the beautifull wedding')
        self.new_image.save_image()
        self.new_image.delete_image()
        images=Image.objects.all()
        self.assertEqual(len(images),1)

    def test_update_method(self):
        self.pic=Image(name ='fa',description='ifoto ya fa')
        self.pic.save_image()
        self.pic=Image(name='KAKA',description='ntugasibe')
        self.pic.update_image(name='KAKA')
        self.pic.save_image()
        images=Image.objects.filter(name='danvic')
        photos=Image.objects.all()
        self.assertEqual(len(images),1)

class CategoryTestclass(TestCase):
    def setUp(self):
        self.pictur=Category(name='grooms')

    def test_instance(self):
        self.assertTrue(isinstance(self.pictur,Category))

    def test_save_method(self):
        self.pictur.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)
    def test_delete_method(self):
        self.new_category=Category(name='bridy')
        self.new_category.save_category()
        self.new_category.delete_category()
        categories=Category.objects.all()
        self.assertEqual(len(categories),0)
    def test_update_category(self):
        self.trust=Category(name ='dressing')
        self.trust.save_category()
        self.trust=Category(name='danser')
        self.trust.save_category()
        self.trust.update_category(name='KAKA')
        categories=Category.objects.filter(name='party')
        self.assertEqual(len(categories),1)

class LocationTestclass(TestCase):
    def setUp(self):
        self.nyanza = Location(name ='nyanza')

    def test_instance(self):
        self.assertTrue(isinstance(self.nyanza, Location))

    def test_save_method(self):
        self.nyanza.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.new_location =Location(name ='KARAMA')
        self.new_location.save_location()
        self.new_location.delete_location()
        locations = Location.objects.all()
        self.assertEqual(len(locations),0)

    def test_update_method(self):
        self.Rwamagana = Location(name='KARAMA')
        self.Rwamagana.save_lacation()
        self.Rwamagana = Location(name = 'Rwamagana')
        self.Rwamagana.save_lacation()
        self.Rwamagana.update_location(name= 'Rwamagana')
        locations = Location.objects.filter(name='Rwamagana')
        self.assertEqual(len(locations),1)

    

