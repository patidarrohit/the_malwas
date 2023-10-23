# Generated by Django 4.2.6 on 2023-10-23 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themalwas', '0005_alter_order_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_type',
            field=models.CharField(choices=[('PICKUP', 'Pickup'), ('HOMEDELIVERY', 'Home Delivery'), ('MEETSOMEWHERE', 'Meed Somewhere')], max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('NEWORDER', 'New Order'), ('INPROGRESS', 'In Progress'), ('ADVANCEMADE', 'Advance Made'), ('ORDERREADY', 'Order Ready'), ('PAYMENTINFULL', 'Payment In Full'), ('DELIVERED', 'Delivered')], max_length=50),
        ),
    ]
