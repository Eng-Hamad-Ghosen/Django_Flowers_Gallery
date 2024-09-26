from django.shortcuts import render
from .models import Flower
# Create your views here.
def home(request):
    flowers = Flower.objects.all() 
    return render(request,'home.html', {'flowers':flowers})

def flower_details(request, slug):
    flower = Flower.objects.get(slug=slug)
    return {'flower':flower}