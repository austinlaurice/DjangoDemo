from django.db import models

# Create your models here.

class Message(models.Model):
    author = models.CharField('發布者', max_length=30)
    content = models.TextField('留言')
    pub_time = models.DateTimeField('發布時間', auto_now_add=True)
