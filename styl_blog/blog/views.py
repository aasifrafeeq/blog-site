from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Blog

def index(request):
    return render(request,'blog/index.html')

def newblog(request):
    return render(request,'blog/new.html')

def dashboard(request):
    try:
        head = Blog.objects.all()
    except Error.DoesNotExist:
        return render(request,'blog/error.html',{'message':"The blog not found."})
    context={
        'head':head,
    }
    return render(request,'blog/dashboard.html',context)

def content(request, heads):
    blog = Blog.objects.get(heading = heads)
    context = {
        'head':heads,
        'blog':blog,
    }
    return render(request,'blog/content.html',context)

def add(request):
    head = request.POST["heading"]
    cont = request.POST["content"]
    if head or cont == None:
        render(request,'blog/error.html',{'message':"The fields must not be empty."})
    new = Blog(heading = head, content=cont)
    new.save()
    return render(request,'blog/success.html')
