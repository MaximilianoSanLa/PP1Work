from django.shortcuts import render
from django.http import HttpResponse

from .models import reviews
# Create your views here.
def home(request):
    searchTerm= request.GET.get('searchReview')
    if searchTerm:
        Reviews= reviews.objects.filter(title_icontains=searchTerm)
    else:
        Reviews= reviews.objects.all()
    return render(request,'home.html', {'searchTerm':searchTerm, 'Reviews':Reviews})
def about(request):
    return render(request, 'about.html')

