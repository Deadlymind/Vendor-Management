# Generated by Django 5.0.4 on 2024-05-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0010_alter_historicalperformance_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='contact_details',
            field=models.TextField(unique=True),
        ),
    ]