from django.conf.urls import url
from . import views

app_name = 'expenses'

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),

    url(r'^expenselist/$', views.expense_list, name='expenses_list'),
    url(r'^expense_create/$', views.expense_create, name='expense_create'),

    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
]