# Generated by Django 3.2.8 on 2021-11-09 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0006_alter_customer_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='billdetail',
            name='item_quantity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
