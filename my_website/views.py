from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse

def index_views(request):
    return render(request, 'my_website/index.html')

def about_views(request):
    return render(request, 'my_website/about.html')

def contact_views(request):
    return render(request, 'my_website/contact.html')

def elements_views(request):
    return render(request, 'my_website/elements.html')

# Create your views here.
