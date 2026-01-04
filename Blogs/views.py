from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
# Create your views here.
def posts_by_category(request,category_id):
    posts = Blog.objects.filter(status = 'Published',category = category_id)
    try:
        category = Category.objects.get(id = category_id)
    except:
        return redirect('home')
    context = {
        'posts':posts,
        'category':category
    }
    return render(request,'posts_by_category.html',context)


def blog(request,slug):
    post = get_object_or_404(Blog,slug=slug)
    context = {
        'blog':post
    }
    return render(request,'blog.html',context)