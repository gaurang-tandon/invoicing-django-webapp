from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from bills.models import Bill, BillDetail, Customer, Item
from django.core import serializers

# Create your views here.

def index(request):
    return render(request, 'index.html')


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.INFO, 'LOGGED OUT')
        return redirect('index')
    else:
        messages.add_message(request, messages.INFO, 'To Logout - Login First')
        return redirect('login_page')

def login_page(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'Already Logged In')
        return redirect('index')
    else :
        if request.method=="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.add_message(request, messages.INFO, 'Invalid Credentials')
    return render(request, 'login_page.html')


def customers(request):
    if request.user.is_authenticated:
        customer_table = Customer.objects.all()
        cust_col_names = Customer.col_names()
        if request.method == "POST":
            my_var = request.POST.get('c_id')
            to_alter_obj = Customer.objects.get(pk = my_var)
            if (request.POST.get('my_button')=='Delete'):
                to_alter_obj.delete()
            elif (request.POST.get('my_button')=='Edit'):
                return render(request, 'edit_customer.html',{
                    'my_cust_id': to_alter_obj.customer_id,
                    'my_cust_name': to_alter_obj.customer_name,
                    'my_cust_add' : to_alter_obj.address,
                    'my_cust_zip' : to_alter_obj.zip_code,
                    'my_cust_phone' : to_alter_obj.phone_number,
                    })
        return render(request, 'customers.html', {
            'customer_table' : customer_table,
            'cust_col_names':cust_col_names,
            })
    else:
        messages.add_message(request, messages.INFO, 'Login First')
        return redirect('login_page')

def add_customer(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            c_name = request.POST.get("name")
            c_address = request.POST.get("address")
            c_pin = request.POST.get("pincode")
            c_phone = request.POST.get("phone")
            new_customer = Customer(customer_name=c_name,address=c_address,zip_code=c_pin,phone_number=c_phone)
            new_customer.save()
            return redirect('customers')
        return render(request, 'add_customer.html')
    else:
        messages.add_message(request, messages.INFO, 'Login First')
        return redirect('login_page')


def edit_customer(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            my_var = request.POST.get('c_id')
            to_alter_obj = Customer.objects.get(pk = my_var)
            to_alter_obj.customer_name = request.POST.get('name')
            to_alter_obj.address = request.POST.get('address')
            to_alter_obj.zip_code = request.POST.get('pincode')
            to_alter_obj.phone_number = request.POST.get('phone')
            to_alter_obj.save()
            return redirect('customers')
    else:
        messages.add_message(request, messages.INFO, 'Login First')
        return redirect('login_page')


def my_bills(request):
    if request.user.is_authenticated:
        bills_table = Bill.objects.all()
        paginator = Paginator(bills_table, 4)
        bills_col_names = Bill.col_names()
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if request.method == "POST":
            my_var = request.POST.get('b_id')
            bill_obj = Bill.objects.get(pk = my_var)
            print(my_var)
            bill_dets = BillDetail.objects.get(bill_id = my_var)
            item_obj = Item.objects.get(pk = bill_dets.item_id_id)
            if (request.POST.get('my_button')=='V'):
                return render(request, 'bill_view.html',{
                    'item_name': item_obj.item_name,
                    'item_id': item_obj.item_id,
                    'item_rate': item_obj.item_rate,
                    'item_quantity': bill_dets.item_quantity,
                    'bill_id': bill_obj.bill_id,
                    'bill_date': bill_obj.bill_date,
                    'bill_customer_name' : bill_obj.customer_id,
                    'bill_amt' : bill_obj.total_amt,
                    })
            elif (request.POST.get('my_button')=='E'):
                customer_table = Customer.objects.all()
                items_table = Item.objects.all()
                cust_id = request.POST.get('customer_id')
                item_id = request.POST.get('item_id')
                return render(request, 'edit_bill.html', {
                    'bill_item_name': item_obj.item_name,
                    'item_id': item_obj.item_id,
                    'item_rate': item_obj.item_rate,
                    'item_quantity': bill_dets.item_quantity,
                    'customer_table': customer_table,
                    'items_table':items_table,
                    'bill_id': bill_obj.bill_id,
                    'bill_date': bill_obj.bill_date,
                    'bill_customer_name' : bill_obj.customer_id,
                    'bill_amt' : bill_obj.total_amt,
                    })
            elif (request.POST.get('my_button')=='D'):
                bill_obj.delete()
        return render(request, 'my_bills.html', {
        'bills_table':bills_table,
        'bills_col_names':bills_col_names,
        'page_obj': page_obj,
        })
    else:
        messages.add_message(request, messages.INFO, 'Login First')
        return redirect('login_page')


def bill_view(request):
    """
    YET TO WRITE CODE
    """
    pass

def edit_bill(request):
    """
    YET TO WRITE CODE
    """
    pass



def my_table(request):
    if request.user.is_authenticated:
        items_table = Item.objects.all()
        items_col_names = Item.col_names()
        return render(request, 'my_table.html', {
            'items_table':items_table,
            'items_col_names':items_col_names,
            })
    else:
        messages.add_message(request, messages.INFO, 'Login First')
        return redirect('login_page')


def new_bill(request):
        if request.user.is_authenticated:
            customer_table = Customer.objects.all()
            items_table = Item.objects.all()
            rate_serializer = serializers.get_serializer("json")()
            rates = rate_serializer.serialize(Item.objects.all())
            # print(rates)
            if request.method == "POST":
                bill_date = request.POST.get('bill_date')
                cust_id = request.POST.get('customer_id')
                count = int(request.POST.get('item_count'))
                # print(count)
                item_id = []
                for i in range(0,count):
                    if(i==(count-1)):
                        var_name = f'item_id'
                        # print(var_name)
                    else:
                        var_name = f'item_id[{i}]'
                    # print(var_name)
                    item = request.POST.get(var_name)
                    # print(item)
                    if item != "":
                        item_id.append(item)
                item_quantity = []
                for i in range(0,count):
                    if(i==(count-1)):
                        var_name = f'item_quantity'
                        # print(var_name)
                    else:
                        var_name = f'item_quantity[{i}]'
                    # print(var_name)
                    quantity = request.POST.get(var_name)
                    # print(item)
                    if quantity != "":
                        item_quantity.append(quantity)
                total_amt = request.POST.get('bill_amt')
                print(f'Bill Date:{bill_date}\nCustomer ID:{cust_id}\nItem ID:{item_id}\nItem Quantity: {item_quantity}\nTotal Amount:{total_amt}')
                new_bill = Bill(total_amt=total_amt, bill_date=bill_date)
                new_bill.save()
                details = BillDetail(item_id=item_id, item_quantity=item_quantity)
                details.save()
                return redirect('new_bill')
            return render(request, 'new_bill.html', {'customer_table':customer_table, 'items_table':items_table, "rates":rates})
        else:
            messages.add_message(request, messages.INFO, 'Login First',)
            return redirect('login_page')