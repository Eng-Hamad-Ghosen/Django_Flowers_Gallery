from django.shortcuts import render
from . forms import RegisterForm
# Create your views here.
def regisetr(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm
    return render(request, 'registration/register.html',{'form':form})