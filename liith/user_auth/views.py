from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import NewUserForm # import from forms.py
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def user_login(request):
    return render(request, 'user_auth/login.html')

def authenticate_user(request):
    """
    Function is used to authenticate the user.

    :param request: data input from the website received via request

    :return: directs user to appropriate page (if user is not found == register new user page; if user authenticated == home page)
    """
    username = request.POST['username']
    password = request.POST['password1']
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(reverse('user_auth:register'))
    else:
        login(request,user)
        return HttpResponseRedirect(reverse('pages:pages_home'))
    
# def show_user(request):
#     print(request.user.username)
#     return render(request, 'user_auth/user.html', {
#                                             "username": request.user.username,
#                                             "password": request.user.password
#                                             })

def register_user(request):
    """
    function creates new user

    :param request: data input from the website received via request

    :return: directs user to appropriate page (if user registration is successful == home page)

    """

    # checks if form is being posted 
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        # checks if form is valid
        if form.is_valid():
            # saves new user
            user = form.save()
            # logs in new user
            authenticate_user(request)
            messages.success(request, 'Registration Successful')
            return redirect('pages:pages_home')
        else:
            messages.error(request, 'Unsuccessful Registration. Invalid Information')
    
    # if form has not been posted, return blank form
    else:
        form = NewUserForm()
        return render(request = request, template_name = 'user_auth/user_registration.html', context = {'register_form':form})
    
def logout_view(request):
    """
    Function logs out user
    """
    logout(request)

        