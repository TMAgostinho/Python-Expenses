from django.contrib import admin
from .models import Category, BankAccountType

# Register your models here.
admin.site.register(Category)
admin.site.register(BankAccountType)