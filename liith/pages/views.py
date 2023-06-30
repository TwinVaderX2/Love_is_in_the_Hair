from django.shortcuts import render
from django.http import HttpResponse

# Views used to direct user to relevant page

def homepage_view(request):
    """
    Function directs user to homepage
    """
    return render(request,'pages/index.html')

def about_us_view(request):
    """
    Function directs user to about us page
    """
    return render(request,'pages/about_us.html')

def price_view(request):
    """
    Function directs user to price list page
    """
    return render(request,'pages/price_list.html')

def contact_us_view(request):
    """
    Function directs user to contact us page
    """
    return render(request,'pages/contact_us.html')

# def test_view(request):
#     """
#     Function directs user to test page
#     """
#     return render(request,'pages/test.html')