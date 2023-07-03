from django.urls import path, include, re_path
from .views import *

# provide app name
app_name = 'user_auth'

urlpatterns = [
                path('', user_login, name='login'),
                path('authenticate_user/', authenticate_user, name='authenticate_user'),
                # path('show_user/',show_user,name = 'show_user'),
                path('register/',register_user, name = 'register'),
                path('logout/',logout_view,name = 'logout'),
]