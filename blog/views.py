from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
# from django.http import HttpResponse, JsonResponse

def blog_views(request):
    posts = Post.objects.filter(status = 1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def single_views(request):
    return render(request, 'blog/blog-single.html')


def test(request, pid):
    post = get_object_or_404(Post,pk=pid)
    context = {'post': post}
    return render(request, 'test.html', context)



def views_post_list(request, pk=None):
    # همه پست‌های منتشر شده
    posts = Post.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')

    selected_post = None

    # اگر pk وجود دارد → نمایش جزئیات پست
    if pk:
        selected_post = get_object_or_404(
            Post,
            pk=pk,
            published_date__lte=timezone.now()
        )
        # افزایش counted_view
        selected_post.counted_views += 1
        selected_post.save()
        selected_post.refresh_from_db()

    return render(request, 'post_list.html', {
        'posts': posts,
        'selected_post': selected_post
    })