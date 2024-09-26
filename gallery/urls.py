from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns = [
    path('Flowers/',views.home,name='home'),
    path('Flowers/<str:slug>/',views.flower_details,name='flower_details'),
]
