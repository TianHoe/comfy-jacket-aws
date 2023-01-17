from django.db import models
from sample_app.models import Product
from users.models import Profile

# Create your models here.
class Order(models.Model):
    # user_id   = models.PositiveSmallIntegerField(default=1, null=False)
    user_id   = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product   = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty       = models.PositiveSmallIntegerField(null=False)
    subtotal  = models.DecimalField(max_digits=6, decimal_places=2, null=False)

    # def __str__(self):
    #     return self.id

    # # get subtotal
    # def get_subtotal(self, *args, **kwargs):
    #     # get the flower values based on id
    #     flower = Product.objects.get(id=self.product.id)
    #     self.subtotal = self.qty * flower.price
    #     # super(Order, self).save(*args, **kwargs)
    #     return self.subtotal