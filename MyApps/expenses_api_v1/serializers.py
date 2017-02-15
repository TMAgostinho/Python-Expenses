from rest_framework import serializers
from expenses.models import Expense, Category

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        exclude = ['user']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
