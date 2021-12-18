# Generated by Django 3.2.8 on 2021-10-29 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('bill_id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('total_amt', models.CharField(max_length=255)),
                ('bill_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=255)),
                ('itme_rate', models.CharField(max_length=100)),
            ],
        ),
    ]