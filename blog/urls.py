from django.urls import path
from blog.views import *
from . import views

app_name = 'blog'

urlpatterns = [
    path('', blog_views, name= 'index'),
    path('single', single_views, name= 'single'),
    path('post-<int:pid>', test , name= 'test'),

        # صفحه اصلی post_list
    path('post_list/', views.views_post_list, name='post_list'),

    # نمایش جزئیات یک پست در همان صفحه
    path('post_list/<int:pk>/', views.views_post_list, name='post_detail_in_list'),

]
