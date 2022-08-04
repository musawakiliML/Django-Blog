from django.db import models

# Create your models here.
class Post(models.Model):
    '''This Model stores the textual content of our posts'''
    text = models.TextField()
    