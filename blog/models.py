from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    #author = models.ForeignKey(models.ForeignKey)
    #category = models.ForeignKey(models.ForeignKey)
    #tag = models.ForeignKey(models.ForeignKey)
    #image = models.ImageField()
    status = models.BooleanField(default = False)
    published_date = models.DateField(null = True)
    counted_views = models.IntegerField(default = 0)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    class Meta:
        ordering = ['-created_date']
#        verbose_name = 'پست'
#        verbose_name_plural = 'پست ها'
    def __str__(self):
        return f'{self.title} {self.id}'