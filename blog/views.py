from django.shortcuts import render,get_object_or_404
from .models import *
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
def blog_view(request,**kwargs):
    #posts = Post.objects.filter(published_date__lte = timezone.now()).exclude(status = 0).order_by('-published_date')
    posts = Post.objects.filter(published_date__lte = timezone.now(),status = 1,).order_by('-published_date')
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_user'):
        posts = posts.filter(author__username = kwargs['author_user'])
    if kwargs.get('tag_name'):
        posts = posts.filter(tag__name__in = [kwargs['tag_name']])
    posts = Paginator(posts,3)
    page_number = request.GET.get('page')
    try:
        posts = posts.page(page_number)
    except PageNotAnInteger:
        posts = posts.page(1)
    except EmptyPage:
        posts = posts.page(1)
    context = {'posts':posts,}
    return render(request,'blog/blog-home.html', context)
def blog_single(request,pid):
    posts = Post.objects.filter(published_date__lte = timezone.now(),status = 1,).order_by('-published_date')
    post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=timezone.now())
    n_post = posts.filter(published_date__gt =post.published_date).last()
    p_post = posts.filter(published_date__lt =post.published_date).first()
    context = {'post':post,'n_post':n_post,'p_post':p_post}
    post.counted_views += 1
    post.save()
    return render(request,'blog/blog-single.html',context)
def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)
def blog_search(request):
    posts = Post.objects.filter(published_date__lte = timezone.now(),status = 1,).order_by('-published_date')
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains = s)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)
