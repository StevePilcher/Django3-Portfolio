from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def all_blogs(request):
    all_blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'all_blogs': all_blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_detail.html',
                  {'blog': blog})
