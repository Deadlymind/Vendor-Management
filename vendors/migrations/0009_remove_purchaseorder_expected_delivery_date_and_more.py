# Generated by Django 5.0.4 on 2024-05-01 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0008_alter_purchaseorder_response_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='expected_delivery_date',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='response_time',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='expected_delivery_date',
        ),
    ]
