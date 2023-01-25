from django.db import models

# Create your models here.
# los id como PK's se crean solos
class Recipe(models.Model):
    name = models.CharField(max_length=2000)
    ingredients = models.CharField(max_length=2000)
    details_link = models.URLField(max_length=2000)
    credits = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name