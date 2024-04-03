from django.contrib import admin
from .models import *
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('id','title','author','status','created_date','published_date','counted_views')
    list_filter = ('status',)
    search_fields = ['title','content']
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']