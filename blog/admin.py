from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('id','title','author','status','created_date','published_date','counted_views')
    list_filter = ('status',)
    search_fields = ['title','content']
    summernote_fields = ['content']
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']