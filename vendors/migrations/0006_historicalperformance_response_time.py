# Generated by Django 5.0.4 on 2024-05-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendors", "0005_purchaseorder_expected_delivery_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalperformance",
            name="response_time",
            field=models.DurationField(blank=True, null=True),
        ),
    ]
