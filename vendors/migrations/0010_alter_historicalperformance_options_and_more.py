# Generated by Django 5.0.4 on 2024-05-01 15:17

import django.db.models.deletion
import vendors.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0009_remove_purchaseorder_expected_delivery_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalperformance',
            options={},
        ),
        migrations.RemoveIndex(
            model_name='historicalperformance',
            name='vendors_his_vendor__165719_idx',
        ),
        migrations.AlterUniqueTogether(
            name='historicalperformance',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='id',
        ),
        migrations.AddField(
            model_name='historicalperformance',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalperformance',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalperformance',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='on_time_delivery',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='response_time',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Time taken to acknowledge POs in hours', max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vendor',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='average_response_time',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='fulfillment_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='on_time_delivery_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='quality_rating_avg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='acknowledgment_date',
            field=models.DateTimeField(blank=True, help_text='Date when vendor acknowledged POs', null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='delivery_date',
            field=models.DateTimeField(help_text='Excepted or Actual delivery date'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='issue_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_number',
            field=models.CharField(help_text='System created PO number', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='quality_rating',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Quality rate out of 10', max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20, null=True, validators=[vendors.models.validate_status]),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='average_response_time',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Average response time in hours', max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='contact_details',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='fulfillment_rate',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Percentage of Successful POs', max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='on_time_delivery_rate',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Percentage of on time delivered POs', max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='quality_rating_avg',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='quality rating out of 10 on each POs', max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.RemoveField(
            model_name='historicalperformance',
            name='date',
        ),
    ]
