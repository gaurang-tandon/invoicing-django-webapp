from django.db import models
# Create your models here.

class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    customer_name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return (self.customer_name)

    def col_names():
        return ('customer_id', 'customer_name', 'address', 'zip_code', 'phone_number')

class Item(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    item_rate = models.CharField(max_length=100)

    def __str__(self):
        return (self.item_name)

    def col_names():
        return ('item_id', 'item_name', 'item_rate')


class Bill(models.Model):
    bill_id = models.BigAutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT)
    total_amt = models.CharField(max_length=255)
    bill_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return (f'Bill ID : {self.bill_id}')

    def col_names():
        return ('bill_id', 'customer_id', 'total_amt', 'bill_date')

class BillDetail(models.Model):
    bill_id = models.ForeignKey(Bill, on_delete=models.PROTECT)
    item_id = models.ForeignKey(Item, on_delete=models.PROTECT)
    item_quantity = models.PositiveIntegerField()

    def __str__(self):
        return (f'Bill ID : {self.bill_id_id}')