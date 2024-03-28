from django.shortcuts import render,get_object_or_404
from .models import Post
from django.utils import timezone
def blog_view(request):
    post_id = list()
    posts = Post.objects.exclude(published_date__gt = timezone.now()).exclude(status = 0)
    post_id.append(post.id for post in posts)
#    posts = Post.objects.filter(status = 1)
    context = {'posts':posts,}
    return render(request,'blog/blog-home.html', context)
def blog_single(request,pid):
    posts = Post.objects.exclude(published_date__gt = timezone.now()).exclude(status = 0).order_by('published_date')
    post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=timezone.now())
    context = 0
    l_index = len(posts) - 1
    for p in range(len(posts)):
        if post.id == posts[p].id and post.id != posts[l_index].id:
            n_post = posts[p+1]
            context = {'post':post,'n_post':n_post}
            if posts[0].id != post.id:
                p_post = posts[p-1]
                context = {'post':post,'n_post':n_post,'p_post':p_post}
                break
        elif post.id == posts[p].id and post.id != posts[0].id:
            p_post = posts[p-1]
            context = {'post':post,'p_post':p_post }
            if posts[l_index].id != post.id:
                n_post = posts[p+1]
                context = {'post':post,'n_post':n_post,'p_post':p_post}
                break
    if context == 0:
        context = {'post':post}
    post.counted_views += 1
    post.save()
    return render(request,'blog/blog-single.html',context)