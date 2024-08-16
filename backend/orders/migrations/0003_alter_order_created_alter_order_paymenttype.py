# Generated by Django 5.0.7 on 2024-08-12 07:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_customer_order_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='paymentType',
            field=models.CharField(choices=[('cash', 'cash'), ('card', 'card')], max_length=60),
        ),
    ]
