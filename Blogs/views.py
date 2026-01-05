from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
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

def search(request):
    keyword = request.GET['keyword']
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | 
                                Q(blog_body__icontains=keyword) | Q(author__username__icontains = keyword) | 
                                Q(category__category_name__icontains = keyword), status = 'Published')
    context = {
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request,'search.html',context)