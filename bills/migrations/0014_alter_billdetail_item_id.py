# Generated by Django 3.2.8 on 2021-11-09 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0013_alter_billdetail_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billdetail',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.item'),
        ),
    ]
