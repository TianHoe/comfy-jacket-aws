from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from datetime import datetime

# Main model
class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Bouquet(models.Model):
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=300, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField(blank=False,null=False)
    description = RichTextField(blank=True, null=True)
    time_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name