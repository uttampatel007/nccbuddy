from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('contribute/', views.contribute, name='contribute'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('guidelines/', views.guidelines, name='guidelines'),  
    path('about/', views.about, name='about'),  
    path('facts/',views.facts,name='facts')

]

