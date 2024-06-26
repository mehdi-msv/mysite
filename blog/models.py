from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
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
    tag = TaggableManager()
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    status = models.BooleanField(default = False)
    published_date = models.DateTimeField(null = True)
    counted_views = models.IntegerField(default = 0)
    login_required = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    class Meta:
        ordering = ['-published_date']
#        verbose_name = 'پست'
#        verbose_name_plural = 'پست ها'

    def __str__(self):
        return f'{self.title} {self.id}'
    
    def get_absolute_url(self):
        return reverse("blog:single", kwargs={"pid": self.id})

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return f'{self.name} {self.email}'