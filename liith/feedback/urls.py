from django.urls import path, include, re_path
from .views import *
# provide app name
app_name = 'feedback'

urlpatterns = [
    path('', feedback_home, name ='feedback_home'),  
    path('review/',review_rate, name = "review_rate"),
]