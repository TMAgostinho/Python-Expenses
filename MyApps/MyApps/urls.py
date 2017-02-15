"""MyApps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url

from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns
from expenses_api_v1.views.auth import AuthView
from expenses_api_v1.views.expense import ExpenseApiGeneric
from expenses_api_v1.views.category import CategoryApiGeneric

urlpatterns = [

    # API
    url(r'^auth/', AuthView.as_view(), name='auth-view'),
    url(r'^api/v1/expense/$', ExpenseApiGeneric.as_view(), name='expense-api-list'),
    url(r'^api/v1/expense/(?P<expense_id>[0-9]+)/$', ExpenseApiGeneric.as_view(), name='expense-api-detail'),
    url(r'^api/v1/category/$', CategoryApiGeneric.as_view(), name='category-api-list'),
    url(r'^api/v1/category/(?P<category_id>[0-9]+)/$', CategoryApiGeneric.as_view(), name='category-api-detail'),

    url(r'^admin/', admin.site.urls),
    #Web App
    #url(r'^expenses/', include('expenses.urls')),
    #url(r'^', include('expenses.urls')),

    #url(r'^', TestView.as_view(), name='test-view'),

]
urlpatterns = format_suffix_patterns(urlpatterns)