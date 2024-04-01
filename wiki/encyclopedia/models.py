from typing import Iterable
from django.db import models, migrations
from django.utils.text import slugify

#add the user model
# Create your models here.
class Entries(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(default="")
    
    def __str__(self):
        return f"{self.title}, {self.content}"