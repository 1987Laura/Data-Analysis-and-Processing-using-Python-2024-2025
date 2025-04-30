from django.db import models

# Create your models here.

###Product, title, description, slug


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null = True)
    slug = models.SlugField(null = True)

    def __str__(self):
        return self.title
