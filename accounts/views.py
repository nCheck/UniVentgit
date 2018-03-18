from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import CollegeForm
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