from django.shortcuts import render
from .models import Flower
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    flowers = Flower.objects.all() 
    return render(request,'home.html', {'flowers':flowers})

def flower_details(request, slug):
    flower = Flower.objects.get(slug=slug)
    return render (request, 'flower_details.html', {'flower':flower})