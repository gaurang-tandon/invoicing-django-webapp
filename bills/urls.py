from django.contrib import admin
from django.urls import path
from bills import views

urlpatterns = [
    path('', views.index , name='index'),
    path('my_bills', views.my_bills , name='my_bills'),
    path('bill_view', views.bill_view, name='bill_view'),
    path('edit_bill', views.edit_bill, name='edit_bill'),
    path("login_page", views.login_page, name='login_page'),
    path("logout_page", views.logout_page, name='logout_page'),
    path("customers", views.customers, name='customers'),
    path("add_customer", views.add_customer, name='add_customer'),
    path("edit_customer", views.edit_customer, name='edit_customer'),
    path('my_table', views.my_table, name='my_table'),
    path("new_bill", views.new_bill, name='new_bill'),
]