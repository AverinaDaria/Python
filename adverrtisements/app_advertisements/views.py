from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement


def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return HttpResponse(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')
# Create your views here.
