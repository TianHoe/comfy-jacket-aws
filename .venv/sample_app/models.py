from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from datetime import datetime

# Category model
class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

# Create your models here.
class Product(models.Model):
    name         = models.CharField(max_length=200, null=False)
    image        = models.ImageField(null=False, blank=False)
    desc         = RichTextField(default='This product has no description yet.')
    stock        = models.PositiveSmallIntegerField(null=False)
    price        = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    category     = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)
    time_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    def get_detail_url(self, *args, **kwargs):
        return reverse("flower_details", kwargs={"my_id": self.id})

