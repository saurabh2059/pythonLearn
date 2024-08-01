from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length  = 50)
    description = models.TextField()
    username = models.CharField(max_length=50 , null=True)

    def __str__(self):
        return f"{self.title} by  .....{self.username}"
    
