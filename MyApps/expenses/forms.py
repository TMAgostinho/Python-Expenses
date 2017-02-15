from django import forms
from django.contrib.auth.models import User
from .models import Expense

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ExpenseForm(forms.ModelForm):
    #Podia ter aqui os campos caso fossem diferentes da base de dados
    class Meta:
        model = Expense
        fields = ['description', 'amount', 'date', 'categoryId']