# Generated by Django 4.2.6 on 2023-10-23 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themalwas', '0004_alter_order_delivery_type_alter_order_item_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='item_name',
            field=models.CharField(max_length=100),
        ),
    ]
