from django.db import models

class Location(models.Model):
  name= models.CharField(max_length=20)

  def __str__(self):
    return self.name
    try:
      Location = Location.objects.get(name = 'KAKIRU')
      print('Location found')
    except DoesNotExist:
      print('Location was not found')

  class Meta:
        ordering = ['name']

  def save_lacation(self):
    self.save()

  def delete_location(self):
    Location.objects.filter(id = self.pk).delete()

  def update_location(self, **kwargs):
    self.objects.filter(id = self.pk).update(**kwargs)
  
class Category(models.Model):
    name = models.CharField(max_length=15)
    Category_image = models.ImageField(upload_to = 'photos/',null=True)

    def __str__(self):

        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        Category.objects.filter(id = self.pk).delete()

    def update_category(self,**kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)

    @classmethod
    def search_by_name(cls,search_term):
      gallery = cls.objects.filter(name=search_term)
      return gallery

    
    
    

class Image(models.Model):
    image= models.ImageField(upload_to = 'photos/', null = True)
    name=  models.CharField(max_length=20)
    description = models.CharField(max_length=60)
    category = models.ForeignKey('Category', on_delete = models.CASCADE, null='True', blank=True)
    location = models.ForeignKey('Location', on_delete = models.CASCADE, null='True', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    def save_image(self):
        self.save()
       

    def delete_image(self):
        Image.objects.filter(id = self.pk).delete()

    def update_image(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)

    @classmethod
    def all_gallery(cls):
      photos = cls.objects.all()
      return photos

    @classmethod
    def photo_locations(cls):
      photos = cls.objects.order_by('location')
      return photos

    @classmethod
    def photo_categories(cls):
      photos = cls.objects.order_by('category')
      return photos
    
    @classmethod
    def todays_gallery(cls):
        today = dt.date.today()
        gallery = cls.objects.filter(pub_date__date = today)
        return gallery

    @classmethod
    def days_gallery(cls,date):
        gallery = cls.objects.filter(pub_date__date = date)
        return gallery

    

    

class Meta:
        ordering = ['name']

