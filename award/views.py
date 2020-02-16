from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .forms import *
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views  here.
@login_required(login_url='/accounts/login/')
def home(request):

    return render (request,'home.html')

def search(request):

    return render(request,'search.html')