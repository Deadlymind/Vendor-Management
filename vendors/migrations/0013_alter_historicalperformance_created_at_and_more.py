# Generated by Django 5.0.4 on 2024-05-01 15:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendors", "0012_alter_historicalperformance_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalperformance",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="purchaseorder",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="purchaseorder",
            name="issue_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="purchaseorder",
            name="order_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
