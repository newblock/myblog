from django.db import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(default='无标题',max_length=50)
    image = models.ImageField(default='default.png',upload_to='image/')
    desc = models.CharField(default='作品简介',max_length=100)

    def __str__(self):
        return self.title