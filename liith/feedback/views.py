from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Review


# code here:
def feedback_home(request):
    feedback_list = Review.objects.all()

    return render(request, 'feedback/feedback_home.html', {'feedback_list': feedback_list})

@login_required(login_url='/user_auth/')
def review_rate(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        rate = request.POST.get('rating')
        user = request.user
        Review(user = user, comment = comment, rate = rate).save()

        return HttpResponseRedirect(reverse('feedback:feedback_home'))


