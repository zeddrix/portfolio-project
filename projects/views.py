from django.shortcuts import render
from .models import Projects

def projects(request):
    projects = Projects.objects
    return render(request, 
    'projects/projects.html', 
    {'projects':projects})