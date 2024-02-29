from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64
from .models import reviews
# Create your views here.
def home(request):
    searchTerm= request.GET.get('searchMovie')
    if searchTerm:
        Reviews= reviews.objects.filter(title=searchTerm)
    else:
        Reviews= reviews.objects.all()
    return render(request,'home.html', {'searchTerm':searchTerm, 'Reviews':Reviews})
def about(request):
    return render(request, 'about.html')
def signup(request):
    email=request.Get.get('email')
    return render(request,'signup.html',{'email':email})
def statistics_view(request):
    matplotlib.use('Agg')
    years= reviews.objects.values_list('year', flat=True).distinct().order_by('year')
    
    movie_counts_by_year= {}
    for year in years:
        if year:
            movies_in_year=  reviews.objects.filter(year=year)
        else:
             movies_in_year= reviews.objects.filter(year__isnull=True)
             year="None"
        count=movies_in_year.count()
        movie_counts_by_year[year]=count
    bar_width=0.5
    bar_positions = range(len(movie_counts_by_year))
    

    plt.bar(bar_positions ,movie_counts_by_year.values() , width=bar_width, align='center')
    
    plt.title('Movies per year')
    plt.xlabel('Year')
    plt.ylabel('Number of movies')
    
    plt.xticks(bar_positions, movie_counts_by_year.keys(),rotation=90)
    
    plt.subplots_adjust(bottom=0.3)
    
    buffer= io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    image_png= buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    print(graphic)
    graphic=graphic.decode('utf-8')
    return render(request, 'statistics.html',{'graphic':graphic})


def statistics_view2(request):
    matplotlib.use('Agg')
    years= reviews.objects.values_list('genre', flat=True).distinct().order_by('genre')
    movie_counts_by_year= {}
    for year in years:
        if year:
            movies_in_year=  reviews.objects.filter(genre=year)
        else:
            movies_in_year= reviews.objects.filter(genre__isnull=True)
            year="None"
        count=movies_in_year.count()
        movie_counts_by_year[year]=count
    bar_width=0.5
    bar_spacing=0.5
    bar_positions = range(len(movie_counts_by_year))
    

    plt.bar(bar_positions,movie_counts_by_year.values(),width=bar_width, align='center')
    plt.title('Movies per genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of movies per genres')
    plt.xticks(bar_positions, movie_counts_by_year.keys(),rotation=90)
    plt.subplots_adjust(bottom=0.3)
    buffer= io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    image_png= buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic=graphic.decode('utf-8')
    return render(request, 'statistics2.html',{'graphic':graphic})
