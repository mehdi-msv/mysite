from django import template
from blog.models import *
from django.utils import timezone
register = template.Library()
@register.inclusion_tag('blog/blog-popular.html')
def blog_latest(args=3):
    posts = Post.objects.filter(status=1,published_date__lte = timezone.now()).order_by('-published_date')[:args]
    return {'posts':posts}
@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status = 1)
    categories = Categories.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category = name).count()
    return {'categories': cat_dict}