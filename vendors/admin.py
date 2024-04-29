from django.contrib import admin
from .models import Vendor, PurchaseOrder, HistoricalPerformance

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
    search_fields = ('name', 'vendor_code')
    list_filter = ('on_time_delivery_rate', 'quality_rating_avg')

class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number', 'vendor', 'order_date', 'delivery_date', 'status')
    search_fields = ('po_number', 'vendor__name')
    list_filter = ('status', 'order_date')
    date_hierarchy = 'order_date'

class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'date', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
    search_fields = ('vendor__name',)
    list_filter = ('date',)
    date_hierarchy = 'date'

admin.site.register(Vendor, VendorAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(HistoricalPerformance, HistoricalPerformanceAdmin)
