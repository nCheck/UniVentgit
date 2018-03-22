from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import logout
from django.views.generic.base import View

from accounts.models import College
from .forms import CollegeForm, SignUpForm


# Create your views here.
def index(request):
    return render(request , 'accounts/index.html' ,context=None)

def register_college(request):
    if request.method == "POST":
        form = CollegeForm(request.POST , request.FILES)
        if form.is_valid():
            form.save(commit=True)

            return render(request , 'accounts/index.html' ,context=None)
    else:
        form = CollegeForm()
    return render(request , 'accounts/register_college.html' , {'form':form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.location = form.cleaned_data.get('location')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        print("form not valid")
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


## ##

class CollegeListView(ListView):
    template_name = 'accounts/colleges.html'
    model = College

class CollegeDetailView(DetailView):
    model = College

