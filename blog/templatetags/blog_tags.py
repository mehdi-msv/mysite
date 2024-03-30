from django import template
from blog.models import Post
from django.utils import timezone
register = template.Library()
@register.inclusion_tag('blog/blog-popular.html')
def blog_latest(args=3):
    posts = Post.objects.filter(status=1,published_date__lte = timezone.now()).order_by('-published_date')[:args]
    return {'posts':posts}