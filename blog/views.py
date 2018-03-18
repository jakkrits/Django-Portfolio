from django.shortcuts import render, get_object_or_404
import datetime as dt
from .models import Blog


def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog/blog.html', context=context)


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog_detail,
    }
    return render(request, 'blog/detail.html', context)
