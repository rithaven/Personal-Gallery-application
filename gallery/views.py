import datetime as dt
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Category

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Best Gallery ')


def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def gallery_of_day(request):
    date = dt.date.today()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Photos for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

# View Function to present news from past days
def past_days_gallery(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(gallery_today)

    gallery = Image.days_gallery(date)
    return render(request, 'all-gallery/past-gallery.html',{"date": date,"gallery":gallery})

def gallery_today(request):
    date = dt.date.today()
    gallery = Image.todays_gallery()
    return render(request, 'all-gallery/today-gallery.html', {"date": date,"gallery":gallery})

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def gallery_of_day(request):
    date = dt.date.today()
    return render(request, 'all-gallery/today-gallery.html', {"date": date,})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Category.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"categories":searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gallery/search.html',{"message":message})

def category(request,category_id):
    try:
        category = Category.objects.get(id = category_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-gallery/category.html", {"category":category})