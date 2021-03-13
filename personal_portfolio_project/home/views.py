from django.shortcuts import render
from projects.models import Project


# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, 'home/home.html', {'projects': projects})
