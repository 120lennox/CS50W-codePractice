from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    enter_tasks = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.text_tasks