from django.db import models
from django.core.validators import EmailValidator


class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.model})"


class BaseNetwork(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(validators=[EmailValidator()])
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='suppliers')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Factory(BaseNetwork):
    products = models.ManyToManyField(Product, related_name='factories')


class RetailNetwork(BaseNetwork):
    products = models.ManyToManyField(Product, related_name='retail_networks')
    supplier = models.ForeignKey(Factory, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='retail_networks')

class Entrepreneur(BaseNetwork):
    products = models.ManyToManyField(Product, related_name='entrepreneurs')
    supplier = models.ForeignKey(RetailNetwork, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='entrepreneurs')