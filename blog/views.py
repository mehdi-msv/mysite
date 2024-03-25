from django.shortcuts import render
from .models import Post
def blog_view(request):
    posts = Post.objects.filter(status = 1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html', context)
def blog_single(request):
    posts = Post.objects.filter(status = 1)
    context = {'posts':posts}
    return render(request,'blog/blog-single.html',context)