from django.shortcuts import render,redirect,get_object_or_404
from Blogs.models import *
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from .forms import *
# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
        'category_count':category_count,
        'blogs_count':blogs_count
    }

    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html')

def add_categories(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form':form
    }
    return render(request,'dashboard/add_categories.html',context)

def edit_categories(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST,instance=category) # if we didn't use instance here it will work as add category
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form':form,
        'pk':pk
    }
    return render(request,'dashboard/edit_categories.html',context)

def del_categories(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')


def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'dashboard/posts.html',context)

def add_posts(request):
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # temporarily save the form into the actual object
            title = form.cleaned_data['title']
            post.author = request.user
            post.save() # if we don't save the post here we won't be able to use the post.id later below
            post.slug = slugify(title) + '-' + str(post.id) #to create a unique slug 
            post.save()
            return redirect('posts')
        else:
            print('invalid form',form.errors)
    form = BlogForm()
    context = {
        'form':form
    }
    return render(request,'dashboard/add_posts.html',context)

def edit_posts(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    if request.method == "POST":
        post_form = BlogForm(request.POST,request.FILES,instance=post)
        if post_form.is_valid():
            post = post_form.save()
            title = post_form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id) # to ensure the slug is always unique
            post.save()
            return redirect('posts')
    form = BlogForm(instance=post)
    context = {
        'form':form,
        'pk':pk
    }
    return render(request,'dashboard/edit_posts.html',context)


def del_posts(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')
