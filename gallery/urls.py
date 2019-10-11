from django.conf.urls import url
from . import views

urlpatterns=[
   
    url('^$',views.gallery_of_day,name='galleryToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_gallery,name = 'pastGallery'),
    url(r'^search/', views.search_results, name='search_results')
]