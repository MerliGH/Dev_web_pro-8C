from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Bank(models.Model):
    bank_name = models.CharField(max_length=16, default="Generic Banck Name")
    address = models.CharField(max_length=32, default="Generic Bank Address")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.bank_name
    


class Currency(models.Model):
    currency_name = models.CharField(max_length=16, default="Generic Currency Name")
    short_name = models.CharField(max_length=4, default="GC")
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.currency_name} : {self.short_name}"




class Account(models.Model):
    account_name = models.CharField(max_length=16, default="Generic Account Name")
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    

    def __str__(self):
        return self.account_name
    


class CategoryProvider(models.Model):
    category_name = models.CharField(max_length=16, default="Generic Category Name")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name
    


class Provider(models.Model):
    provider_name = models.CharField(max_length=32, default="Generic Provider Name")
    category = models.ForeignKey(CategoryProvider, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.provider_name
    



METHOD_CHOICES = (
    ("CH", "CASH"),
    ("TF", "TRANSFER"),
    ("CR", "CREDIT"),
)

class Payment(models.Model):
    payment_name = models.CharField(max_length=32, default="Generic Payment Name")
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    timestamp = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=16, choices=METHOD_CHOICES)

    def __str__(self):
        return self.payment_name



"""
Bancos
Divisas /// mx us eu le
Cuentas Banco
    banco
    tipos divisas

category provider

Proveedores
    category

Payments
    cuentas banco
    proveedores
"""