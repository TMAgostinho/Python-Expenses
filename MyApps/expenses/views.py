from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .forms import UserForm, ExpenseForm
from .models import Expense


# Create your views here.
def dashboard(request):
    if request.user.is_authenticated():
        expenses = Expense.objects.filter(user=request.user)
        return render(request, 'expenses/index.html', {'expenses': expenses})
    else:
        return render(request, 'common/login.html')

#Expenses Views
def expense_detail(request):
    if not request.user.is_authenticated():
        return render(request, 'common/login.html')
    else:
        return render(request, 'expenses/index.html')

def expense_create(request):
    if not request.user.is_authenticated():
        return redirect(reverse('expenses:login_user'))
    else:
        form = ExpenseForm(request.POST or None)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user

            #Define moviment type
            expense.isCredit = expense.amount > 0
            expense.save()
            return redirect(reverse('expenses:dashboard'))

    return render(request, 'expenses/expense_create.html', {'form': form})

def expense_list(request):
    if not request.user.is_authenticated():
        return render(request, 'common/login.html')
    else:
        return render(request, 'expenses/index.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'common/login.html', context)

def login_user(request):
    print('login_user')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('expenses:dashboard'))
            else:
                return render(request, 'common/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'common/login.html', {'error_message': 'Invalid login'})
    return render(request, 'common/login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                expenses = Expense.objects.filter(user=request.user)
                return render(request, 'expenses/index.html', {'expenses': expenses},)
    return render(request, 'common/register.html', { 'form': form, })