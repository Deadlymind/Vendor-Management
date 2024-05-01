from rest_framework import serializers
from .models import Vendor, PurchaseOrder, HistoricalPerformance

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            'id', 'name', 'contact_details', 'address', 'vendor_code',
            'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time',
            'fulfillment_rate', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    vendor_details = serializers.SerializerMethodField()

    class Meta:
        model = PurchaseOrder
        fields = [
            'po_number', 'vendor', 'vendor_details', 'order_date', 'delivery_date',
            'items', 'quantity', 'status', 'quality_rating', 'issue_date',
            'acknowledgment_date', 'response_time', 'on_time_delivery', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'po_number']

    def get_vendor_details(self, obj):
        # Assuming simple details are needed, adjust fields as necessary
        serializer = VendorSerializer(obj.vendor)
        return serializer.data

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = [
            'created_by', 'vendor', 'on_time_delivery_rate', 'quality_rating_avg',
            'average_response_time', 'fulfillment_rate', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
