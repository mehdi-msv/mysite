from django.contrib import admin
from .models import Contact
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('email','subject','created_date')
    search_fields = ('email','subject','message')
    list_filter = ['email']