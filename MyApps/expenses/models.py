from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class BankAccountType(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=6)
    
    def __str__(self):
        return self.code + " - " + self.name 

class Expense(models.Model):
    user = models.ForeignKey(User, default=1)
    categoryId = models.ForeignKey(Category, default=1)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    isCredit = models.BooleanField(default=False)
    description = models.CharField(max_length=64, null=True)

class BankAccount(models.Model):
    user = models.ForeignKey(User, default=1)
    username = models.CharField(max_length=32, null=True)
    password = models.CharField(max_length=32, null=True)
    cardNumber = models.CharField(max_length=32, null=True)
    iban = models.CharField(max_length=32, null=True)