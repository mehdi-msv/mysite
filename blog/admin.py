from django.contrib import admin
from .models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    fields = ('id','title')
    list_display = ('title','status','created_date','counted_views')
    list_filter = ('status',)
    search_fields = ['title','content']