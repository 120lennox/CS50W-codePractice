from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    User = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    Task_head = models.CharField(max_length=50)
    Task_body = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.Task_head}, {self.Task_body}"