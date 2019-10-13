# import datetime as dt
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Image

# Create your views here.
def myphoto(request):
    captured=Image.captured()
    print(captured)
    return render (request, 'all-gallery/images.html',{"captured":captured})

# def convert_dates(dates):

#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)

#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

#     # Returning the actual day of the week
#     day = days[day_number]
#     return day

# def gallery_of_day(request):
#     date = dt.date.today()

#     # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
#     day = convert_dates(date)
#     html = f'''
#         <html>
#             <body>
#                 <h1>Photos for {day} {date.day}-{date.month}-{date.year}</h1>
#             </body>
#         </html>
#             '''
#     return HttpResponse(html)

# # View Function to present news from past days
# def past_days_gallery(request, past_date):
#     try:
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()
#         assert False

#     if date == dt.date.today():
#         return redirect(gallery_today)

#     gallery = Image.days_gallery(date)
#     return render(request, 'all-gallery/past-gallery.html',{"date": date,"gallery":gallery})

# def gallery_today(request):
#     date = dt.date.today()
#     gallery = Image.todays_gallery()
#     return render(request, 'all-gallery/today-gallery.html', {"date": date,"gallery":gallery})

# def gallery_of_day(request):
#     date = dt.date.today()
#     return render(request, 'all-gallery/today-gallery.html', {"date": date,})

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
    foto = Image.get_foto(image_id)
    return render(request,'all-gallery/one-image.html',{"foto":foto})