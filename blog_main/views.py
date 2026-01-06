from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .forms import *


from Blogs.models import Category,Blog
from assignments.models import *
def home(request):
    categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured = True,status = 'Published')
    posts = Blog.objects.filter(is_featured = False,status = 'Published').order_by('-created_at')
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'categories':categories,
        'featured_post':featured_post,
        'posts':posts,
        'about':about,

    }
    return render(request,'home.html',context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    context = {
        'form':form
    }
    return render (request,'register.html',context)


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']            
            password = form.cleaned_data['password']            
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                next = request.POST.get('next')
                if next:
                    return redirect(next) 
                return redirect('home')
                
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render (request,'login_page.html',context)

def logout_page(request):
    logout(request)
    return redirect('home')