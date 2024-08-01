from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=20, null=False)
    email_address = models.EmailField(null=True)

    def __str__(self) :
        return  f"name : {self.name} registered"