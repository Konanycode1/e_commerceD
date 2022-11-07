
from django.urls import reverse
from django.db import models

# Create your models here.
"""
Produit
- nom
- Prix
- Description
- La quantité du stock
- Image

"""
class Produit(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="produits", blank=True, null=True)

    def __str__(self):
        # return f"{self.name} ({self.stock})"
        return self.name 
    def get_absolute_url(self):
        return reverse("produit", kwargs={"slug":self.slug})  