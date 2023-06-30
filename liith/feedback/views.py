from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Review


# Views directing user to relevant page

def feedback_home(request):
    """
    function directs user to feedback home page
    """

    # create new list containing all objects in Review model
    feedback_list = Review.objects.all()

    return render(request, 'feedback/feedback_home.html', {'feedback_list': feedback_list})

# user must be loged in to provide review
@login_required(login_url='/user_auth/')
def review_rate(request):
    """
    function to create new review

    :return: directs user back to feedback home page (refresh)
    """

    # checks if users submitted review
    if request.method == "POST":
        comment = request.POST.get('comment')
        rate = request.POST.get('rating')
        user = request.user
        # create new review using class/model
        Review(user = user, comment = comment, rate = rate).save()

        return HttpResponseRedirect(reverse('feedback:feedback_home'))


