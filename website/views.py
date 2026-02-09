from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index_views(request):
    return HttpResponse('<h1>Home page</h1>')

def about_views(request):
    return HttpResponse('<h1>About page</h1>')

def contact_views(request):
    return HttpResponse('<h1>Contact page</h1>')

# Create your views here.
