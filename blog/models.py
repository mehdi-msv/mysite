from django.db import models
from django.contrib.auth.models import User
class Categories(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Tags(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    category = models.ManyToManyField(Categories)
    tag = models.ManyToManyField(Tags)
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    status = models.BooleanField(default = False)
    published_date = models.DateField(null = True)
    counted_views = models.IntegerField(default = 0)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    class Meta:
        ordering = ['-published_date']
#        verbose_name = 'پست'
#        verbose_name_plural = 'پست ها'
    def __str__(self):
        return f'{self.title} {self.id}'