# Generated by Django 4.2.6 on 2023-10-23 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themalwas', '0007_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_type',
            field=models.CharField(choices=[('Pickup', 'Pickup'), ('HOMEDELIVERY', 'Home Delivery'), ('MEETSOMEWHERE', 'Meed Somewhere')], max_length=20),
        ),
    ]
