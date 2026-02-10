from django.urls import path
from my_website.views import *

urlpatterns = [
    path('', index_views),
    path('about', about_views),
    path('contact', contact_views),

]
