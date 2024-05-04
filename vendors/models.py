from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Choices for status field
STATUS_CHOICES = (
    ("Pending", "Pending"),
    ("Completed", "Completed"),
    ("Cancelled", "Cancelled"),
)


# Validator for status field
def validate_status(value):
    """Validates that the provided value is a valid order status."""
    valid_choices = [choice[0] for choice in STATUS_CHOICES]
    if value not in valid_choices:
        raise ValueError("Invalid order status")
    return True


# Vendor model for vendor information
class Vendor(models.Model):
    """
    Represents a vendor in the system with related
    details and performance metrics.
    """

    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, unique=True)
    contact_details = models.TextField(unique=True)
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Percentage of on time delivered POs",
    )
    quality_rating_avg = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Quality rating out of 10 on each POs",
    )
    average_response_time = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Average response time in hours",
    )
    fulfillment_rate = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Percentage of Successful POs",
    )

    def __str__(self):
        return self.name


# PurchaseOrder model for purchase order information
class PurchaseOrder(models.Model):
    """
    Tracks purchase orders including details about vendors,
    order and delivery dates, and status.
    """

    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    po_number = models.CharField(
        max_length=50, primary_key=True, help_text="System created PO number"
    )
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)
    delivery_date = models.DateTimeField(
        help_text="Expected or Actual delivery date"
    )
    items = models.JSONField()
    quantity = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        null=True,
        blank=True,
        validators=[validate_status],
        default="Pending",
    )
    quality_rating = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Quality rate out of 10",
    )
    issue_date = models.DateTimeField(default=timezone.now)
    acknowledgment_date = models.DateTimeField(
        null=True, blank=True, help_text="Date when vendor acknowledged POs"
    )
    response_time = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Time taken to acknowledge POs in hours",
    )
    on_time_delivery = models.BooleanField(default=False)

    # Custom save method to handle logic on save
    def save(self, *args, **kwargs):
        # Generate PO number if not provided
        if not self.po_number:
            today = timezone.now().date()
            last_po = (
                PurchaseOrder.objects.filter(vendor=self.vendor)
                .order_by("-order_date")
                .first()
            )
            if last_po:
                last_number = int(last_po.po_number.split("-")[-1])
                new_number = last_number + 1
            else:
                new_number = 1
            self.po_number = f'{self.vendor.vendor_code}-{today.strftime("%Y%m%d")}-{new_number:04d}'

        # Calculate response time and update on-time delivery status
        if self.issue_date and self.acknowledgment_date:
            acknowledgment_date = self.acknowledgment_date.replace(tzinfo=None)
            issue_date = self.issue_date.replace(tzinfo=None)
            response_time = (acknowledgment_date - issue_date).total_seconds()
            self.response_time = response_time / 3600

        if self.status == "Completed":
            if self.delivery_date is None:
                self.delivery_date = timezone.now()
                self.on_time_delivery = True
            elif self.delivery_date > timezone.now():
                self.on_time_delivery = True
        else:
            self.quality_rating = 0

        super().save(*args, **kwargs)

    def __str__(self):
        return self.po_number


# HistoricalPerformance model for historical performance data
class HistoricalPerformance(models.Model):
    """
    Stores historical performance data for vendors to track changes over time.
    """

    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    on_time_delivery_rate = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    quality_rating_avg = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    average_response_time = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    fulfillment_rate = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )

    def __str__(self):
        return self.vendor.name
