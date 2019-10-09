from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.

def blog(request):
    blogall = Blog.objects.all()
    return render(request,'blog.html',{'aall':blogall})

def blog_text(request,blog_id):
    #@blogs = Blog.objects.all()
    #blog = Blog.objects.all()[blog_id-1]
    blog = get_object_or_404(Blog,pk = blog_id)
    return render(request,'blog_text.html',{'article':blog})