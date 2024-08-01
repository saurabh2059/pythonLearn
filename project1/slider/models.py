from django.db import models

# Create your models here.

class Slider(models.Model):
    image = models.ImageField(upload_to ="slider/",blank=True, null=True)
    description = models.CharField(max_length=100, null=True)

    def __str__(self) :
        return f"image slider"