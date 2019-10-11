from django.contrib import admin
from .models import Location,Category,Image

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('locations',)

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image)
  
