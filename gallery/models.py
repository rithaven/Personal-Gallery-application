from django.db import models

class Location(models.Model):
  name= models.CharField(max_length=20)

  def __str__(self):
    return self.name
  #   try:
  #     Location = Location.objects.get(name = 'KAKIRU')
  #     print('Location found')
  #   except DoesNotExist:
  #     print('Location was not found')

  # class Meta:
  #       ordering = ['name']

  def save_lacation(self):
    self.save()

  def delete_location(self):
    Location.objects.filter(id = self.pk).delete()

  def update_location(self, **kwargs):
    self.objects.filter(id = self.pk).update(**kwargs)
  
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):

        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        Category.objects.filter(id = self.pk).delete()

    def update_category(self,**kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)

class Image(models.Model):
    image= models.ImageField(upload_to = 'categories/', null = True)
    name=  models.CharField(max_length=20)
    description = models.CharField(max_length=60)
    category = models.ForeignKey('Category', on_delete = models.CASCADE, null='True', blank=True)
    location = models.ForeignKey('Location', on_delete = models.CASCADE, null='True', blank=True)
   

    def __str__(self):
        return self.name
    def save_image(self):
        self.save()
       

    def delete_image(self):
        Image.objects.filter(id = self.pk).delete()

    def update_image(self,**kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)

    @classmethod
    def captured(cls):
      photos = cls.objects.all()
      return photos

    @classmethod
    def images_locations(cls):
      photos = cls.objects.order_by('location')
      return photos

    @classmethod
    def images_categories(cls):
      photos = cls.objects.order_by('category')
      return photos

    @classmethod
    def get_foto(cls,id):
      phot =cls.objects.get(id=id)
      return phot
    
    @classmethod
    def search_by_category(cls,search_term):
      images = cls.objects.filter(category__name__icontains=search_term)
      return images

    class Meta:
       ordering = ['name']

