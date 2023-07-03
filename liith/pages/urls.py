from django.urls import path, include, re_path
from .views import *

# provide app name
app_name = 'pages'

urlpatterns = [
    path('', homepage_view, name='pages_home'),
    path('pricelist/',price_view, name = 'price_list'),
    # path('test/', test_view, name = 'test'),
    path('aboutus/', about_us_view, name='about_us'),
    path('contactus/', contact_us_view, name = 'contact_us'),   
]