from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .forms import *
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model

# Create your views  here.
@login_required(login_url='/accounts/login/')
def home(request):

    return render (request,'home.html')

def search(request):

    return render(request,'search.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES),
        if u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()
        context = {
            'u_form': u_form,
            'p_form': p_form,
    }
    return render(request, 'profile.html', context) 
  