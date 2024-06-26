# Generated by Django 5.0.4 on 2024-05-01 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendors", "0013_alter_historicalperformance_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vendor",
            name="quality_rating_avg",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Quality rating out of 10 on each POs",
                max_digits=8,
                null=True,
            ),
        ),
    ]
