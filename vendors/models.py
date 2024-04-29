from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator



class Vendor(models.Model):
    """
    Represents a vendor with detailed information and performance metrics.
    Stores data related to vendor contact, performance statistics, and identification.

    Fields:
    - name: The name of the vendor.
    - contact_details: Contact information such as phone number and email.
    - address: Physical address of the vendor.
    - vendor_code: Unique identifier for each vendor.
    - on_time_delivery_rate: Percentage rate of deliveries made on time.
    - quality_rating_avg: Average quality rating received from orders.
    - average_response_time: Average time taken by the vendor to respond.
    - fulfillment_rate: Rate of successfully fulfilled orders.
    """
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=100, unique=True, db_index=True)
    on_time_delivery_rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    quality_rating_avg = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return f"{self.name} ({self.vendor_code})"

    def update_performance_metrics(self, **metrics):
        """
        Update performance metrics for a vendor.

        Args:
        - metrics: A dictionary of metric names and their new values.
        """
        try:
            for attr, value in metrics.items():
                setattr(self, attr, value)
            self.save()
        except Exception as e:
            print(f"Error updating vendor metrics: {e}")

class PurchaseOrder(models.Model):
    """
    Represents a purchase order, linking to a Vendor and tracking the order status,
    items, and other metrics related to vendor performance evaluation.

    Fields:
    - po_number: Unique identifier for the purchase order.
    - vendor: ForeignKey link to the Vendor model.
    - order_date: Date when the order was placed.
    - delivery_date: Expected or actual delivery date.
    - items: JSON storing details of the items ordered.
    - quantity: Total quantity of items ordered.
    - status: Current status of the order (pending, completed, canceled).
    - quality_rating: Rating given to the vendor for this specific order.
    - issue_date: Date when the order was issued to the vendor.
    - acknowledgment_date: Date when the order was acknowledged by the vendor.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    po_number = models.CharField(max_length=100, unique=True, db_index=True)
    vendor = models.ForeignKey(Vendor, related_name='purchase_orders', on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"PO {self.po_number} - {self.status}"

    def clean(self):
        """
        Custom validation to ensure delivery date is not before order date.
        """
        if self.delivery_date < self.order_date:
            raise ValidationError("Delivery date cannot be before the order date.")




class HistoricalPerformance(models.Model):
    """
    Tracks historical performance metrics of vendors over time to analyze trends.

    Fields:
    - vendor: ForeignKey link to the Vendor model.
    - date: Date of the performance record.
    - on_time_delivery_rate: Historical on-time delivery rate.
    - quality_rating_avg: Historical average quality rating.
    - average_response_time: Historical average response time.
    - fulfillment_rate: Historical fulfillment rate.
    """
    vendor = models.ForeignKey(Vendor, related_name='historical_performances', on_delete=models.CASCADE)
    date = models.DateTimeField(db_index=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    class Meta:
        unique_together = ('vendor', 'date')
        indexes = [
            models.Index(fields=['vendor', 'date']),
        ]
        get_latest_by = "date"

    def __str__(self):
        return f"{self.vendor.name} Performance on {self.date.strftime('%Y-%m-%d')}"