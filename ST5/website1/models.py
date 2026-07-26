from datetime import datetime
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
