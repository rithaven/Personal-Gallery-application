# import datetime as dt
from django.http  import HttpResponse,Http404
from django.shortcuts import render
from .models import Image

# Create your views here.
def myphoto(request):
    captured=Image.captured()
    print(captured)
    return render (request, 'all-gallery/images.html',{"captured":captured})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"images":searched_images})

    else:
        message = "You haven't searched for anything,write category to search"

    return render(request, 'all-gallery/search.html',{"message":message})

def display_locations_of_images(request):
    fotos=Image.images_locations()
    return render(request,'all-gallery/from.html',{"fotos":fotos})

def display_categories_of_images(request):
    fotos = Image.images_categories()
    return render (request,'all-gallery/imageCategory.html',{"fotos":fotos})
    
def one_photo(request):
    image = Image.get_foto(image_id)
    return render(request,'all-gallery/search.html',{"image":image})