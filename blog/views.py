from django.shortcuts import render,get_object_or_404
from .models import Post
from django.utils import timezone
def blog_view(request):
    posts = Post.objects.exclude(published_date__gt = timezone.now()).exclude(status = 0)
#    posts = Post.objects.filter(status = 1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html', context)
def blog_single(request,pid):
    posts = Post.objects.exclude(published_date__gt = timezone.now()).exclude(status = 0)
    post = get_object_or_404(posts, pk=pid)
    context = {'post':post}
    post.counted_views += 1
    post.save()
    return render(request,'blog/blog-single.html',context)
