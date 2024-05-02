import logging

from django.db import transaction
from django.db.models import Avg, F
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import HistoricalPerformance, PurchaseOrder

# Configure logger
logger = logging.getLogger(__name__)


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_metrics(sender, instance, created, **kwargs):
    if not instance.vendor:
        return

    fields_to_check = [
        "status",
        "quality_rating",
        "acknowledgment_date",
        "delivery_date",
    ]
    if created or any(
        instance.tracker.has_changed(field) for field in fields_to_check
    ):
        with transaction.atomic():
            if instance.status == "Completed":
                update_on_time_delivery_rate(instance.vendor)

            if (
                instance.quality_rating is not None
                and instance.status == "Completed"
            ):
                update_quality_rating_average(instance.vendor)

            if instance.acknowledgment_date is not None:
                update_average_response_time(instance.vendor)

            update_fulfillment_rate(instance.vendor)

            instance.vendor.save()

            HistoricalPerformance.objects.create(
                created_by=instance.created_by,
                vendor=instance.vendor,
                on_time_delivery_rate=instance.vendor.on_time_delivery_rate,
                quality_rating_avg=instance.vendor.quality_rating_avg,
                average_response_time=instance.vendor.average_response_time,
                fulfillment_rate=instance.vendor.fulfillment_rate,
                created_at=timezone.now(),
            )


def update_on_time_delivery_rate(vendor):
    try:
        total_completed = PurchaseOrder.objects.filter(
            vendor=vendor, status="Completed"
        ).count()
        on_time = PurchaseOrder.objects.filter(
            vendor=vendor,
            status="Completed",
            delivery_date__lte=F("order_date"),
        ).count()
        if total_completed > 0:
            vendor.on_time_delivery_rate = (on_time / total_completed) * 100
    except Exception as e:
        logger.error(
            f"Error updating on-time delivery rate for vendor {vendor.id}: {str(e)}"
        )


def update_quality_rating_average(vendor):
    try:
        ratings = PurchaseOrder.objects.filter(
            vendor=vendor, status="Completed", quality_rating__isnull=False
        )
        if ratings.exists():
            vendor.quality_rating_avg = ratings.aggregate(
                Avg("quality_rating")
            )["quality_rating__avg"]
    except Exception as e:
        logger.error(
            f"Error updating quality rating average for vendor {vendor.id}: {str(e)}"
        )


def update_average_response_time(vendor):
    try:
        response_times = PurchaseOrder.objects.filter(
            vendor=vendor, acknowledgment_date__isnull=False
        )
        if response_times.exists():
            total_response_time = sum(
                (rt.acknowledgment_date - rt.issue_date).total_seconds()
                for rt in response_times
            )
            vendor.average_response_time = (
                total_response_time / len(response_times)
            ) / 3600  # Convert seconds to hours
    except Exception as e:
        logger.error(
            f"Error updating average response time for vendor {vendor.id}: {str(e)}"
        )


def update_fulfillment_rate(vendor):
    try:
        total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
        completed_orders = PurchaseOrder.objects.filter(
            vendor=vendor, status="Completed"
        ).count()
        if total_orders > 0:
            vendor.fulfillment_rate = (completed_orders / total_orders) * 100
    except Exception as e:
        logger.error(
            f"Error updating fulfillment rate for vendor {vendor.id}: {str(e)}"
        )
