from django.contrib import admin
from bills.models import Customer, Bill, Item, BillDetail

# Register your models here.

admin.site.register([Customer, Bill, Item, BillDetail])