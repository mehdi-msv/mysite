from django.db import models

# Create your models here.
class Topics(models.Model):
#    text = models.CharField(max_length=200)
    text = 'hello mehdi'
    date_add = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.text