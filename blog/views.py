from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse

def blog_views(request):
    return render(request, 'blog/blog-home.html')

def single_views(request):
    return render(request, 'blog/blog-single.html')


# Create your views here.
