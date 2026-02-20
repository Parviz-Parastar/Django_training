from django.urls import path
from my_website.views import *

app_name = 'my_website'

urlpatterns = [
    path('', index_views, name= 'index'),
    path('about', about_views, name= 'about'),
    path('contact', contact_views, name= 'contact'),
    path('elements', elements_views, name= 'elements'),

]
