from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length  = 50)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} {self.description}"
    
