# Generated by Django 5.0.4 on 2024-05-01 13:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendors", "0004_vendor_expected_delivery_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchaseorder",
            name="expected_delivery_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
