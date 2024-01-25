from django.db import models

# Create your models here.
from django.db import models

class Flower(models.Model):
    flower_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    wong = models.CharField(max_length=50)
    sagun = models.CharField(max_length=50)
    properties = models.TextField()
    image = models.ImageField(upload_to='place_images/')

    def __str__(self):
        return self.name
