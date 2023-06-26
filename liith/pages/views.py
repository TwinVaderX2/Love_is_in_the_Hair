from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage_view(request):

    return render(request,'pages/index.html')

def about_us_view(request):

    return render(request,'pages/about_us.html')

def price_view(request):

    return render(request,'pages/price_list.html')

def contact_us_view(request):

    return render(request,'pages/contact_us.html')

def test_view(request):

    return render(request,'pages/test.html')