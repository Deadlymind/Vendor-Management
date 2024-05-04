from django.contrib import admin

from .models import HistoricalPerformance, PurchaseOrder, Vendor


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    """
    Admin panel for managing vendor information.
    """

    list_display = (
        "id",
        "created_at",
        "updated_at",
        "created_by",
        "name",
        "contact_details",
        "address",
        "vendor_code",
        "on_time_delivery_rate",
        "quality_rating_avg",
        "average_response_time",
        "fulfillment_rate",
    )


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    """
    Admin panel for managing purchase orders.
    """

    list_display = (
        "po_number",
        "vendor",
        "order_date",
        "delivery_date",
        "status",
        "quality_rating",
        "acknowledgment_date",
        "response_time",
        "on_time_delivery",
    )


@admin.register(HistoricalPerformance)
class HistoricalPerformanceAdmin(admin.ModelAdmin):
    """
    Admin panel for managing historical performance metrics.
    """

    list_display = (
        "vendor",
        "on_time_delivery_rate",
        "quality_rating_avg",
        "average_response_time",
        "fulfillment_rate",
    )
