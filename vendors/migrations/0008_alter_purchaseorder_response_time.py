# Generated by Django 5.0.4 on 2024-05-01 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0007_remove_historicalperformance_response_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='response_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
