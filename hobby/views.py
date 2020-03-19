from django.shortcuts import render
from .models import Hobby

def home(request):
    hobbies = Hobby.objects
    return render(request, 
    'hobby/home.html', 
    {'hobbies':hobbies})