from django.db import models

# Create your models here.

class Review(models.Model):
    email = models.EmailField(max_length=100,null=False)
    phoneNo = models.CharField(max_length=50 , null=True)
    review = models.TextField(max_length=300)

    def __str__(self):
        return f" review  by {self.email}"
    

