from django.db import models


# Create your models here.

class Bookmark(models.Model):
    title = models.CharField('Title', max_length=100, blank=True)
    url = models.URLField('URL', unique=True) #유니크 트루???, 앞에 값은 뭐지? 

    def __str__(self):
        return self.title
