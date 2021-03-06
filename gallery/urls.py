from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.myphoto,name = 'myphoto'),
    url(r'^locations/',views.display_locations_of_images,name ='locations'),
    url(r'^categories/',views.display_categories_of_images,name ='categories'),
    url(r'^search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)