from .views import *
from django.urls import path
from blog.feeds import LatestEntriesFeed
app_name = 'blog'

urlpatterns = [
    path('',blog_view,name='blog'),
    path('<int:pid>',blog_single,name='single'),
    path('category/<str:cat_name>',blog_view,name='category'),
    path('author/<str:author_user>',blog_view,name='author'),
    path('search/',blog_search,name='search'),
    path('tag/<str:tag_name>',blog_view,name='tag'),
    path('rss/feed/', LatestEntriesFeed()),

]
