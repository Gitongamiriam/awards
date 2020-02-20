from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .forms import *
from .models import Profile,Project
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer

# Create your views  here.
@login_required(login_url='/accounts/login/')
def home(request):
    projects =Project.show_projects()
    return render (request,'home.html',{'projects':projects})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)


def search(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message, "projects":searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def project(request):
    projects =Project.show_projects()
   
    return render(request,"project.html", {"project":project})        

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.name = current_user
            project.save()
        return redirect('home')
    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})



class ProfileList(APIView):
    def get(self,request,format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile,many = True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self,request,format=None):
        all_project = Project.objects.all()
        serializers = ProjectSerializer(all_project,many = True)
        return Response(serializers.data)       






  