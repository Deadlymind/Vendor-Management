from decimal import Decimal

from django.test import TestCase
from rest_framework.test import APIClient

from vendors.models import HistoricalPerformance, PurchaseOrder, Vendor
from vendors.serializers import (HistoricalPerformanceSerializer,
                                 PurchaseOrderSerializer, VendorSerializer)


class VendorSerializerTest(TestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="Test Vendor",
            contact_details="test@vendor.com",
            address="123 Vendor St",
            vendor_code="V001",
            on_time_delivery_rate=Decimal("98.7"),
            quality_rating_avg=Decimal("4.5"),
            average_response_time=Decimal("24.0"),
            fulfillment_rate=Decimal("75.5"),
        )

    def test_vendor_serializer(self):
        serializer = VendorSerializer(instance=self.vendor)
        data = serializer.data
        self.assertEqual(data["name"], self.vendor.name)
        self.assertEqual(data["contact_details"], self.vendor.contact_details)
        self.assertEqual(data["address"], self.vendor.address)
        self.assertEqual(data["vendor_code"], self.vendor.vendor_code)
        self.assertEqual(data["on_time_delivery_rate"], "98.70")
        self.assertEqual(data["quality_rating_avg"], "4.50")
        self.assertEqual(data["average_response_time"], "24.00")
        self.assertEqual(data["fulfillment_rate"], "75.50")


from decimal import Decimal

from django.test import TestCase
from django.utils import timezone

from vendors.models import PurchaseOrder, Vendor
from vendors.serializers import PurchaseOrderSerializer


class PurchaseOrderSerializerTest(TestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="Test Vendor", vendor_code="V123"
        )
        # Ensure the dates are correctly handled as timezone aware
        self.purchase_order = PurchaseOrder.objects.create(
            vendor=self.vendor,
            order_date=timezone.make_aware(timezone.datetime(2024, 1, 1)),
            delivery_date=timezone.make_aware(timezone.datetime(2024, 1, 5)),
            items={"item1": "test item"},
            quantity=10,
            status="Pending",
            quality_rating=Decimal("4.0"),
            issue_date=timezone.make_aware(timezone.datetime(2024, 1, 1)),
            acknowledgment_date=timezone.make_aware(
                timezone.datetime(2024, 1, 2)
            ),
            response_time=Decimal("24"),
            on_time_delivery=True,
        )

    def test_purchase_order_serializer(self):
        serializer = PurchaseOrderSerializer(instance=self.purchase_order)
        data = serializer.data
        self.assertEqual(data["vendor"], self.vendor.id)
        self.assertEqual(data["vendor_details"]["name"], self.vendor.name)
        self.assertEqual(data["order_date"], "2024-01-01T00:00:00Z")
        self.assertEqual(data["delivery_date"], "2024-01-05T00:00:00Z")
        self.assertEqual(data["quantity"], 10)
        self.assertEqual(data["status"], "Pending")
        self.assertEqual(float(data["quality_rating"]), 0.0)
        self.assertEqual(float(data["response_time"]), 24.0)
        self.assertTrue(data["on_time_delivery"])


class HistoricalPerformanceSerializerTest(TestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="Test Vendor", vendor_code="V123"
        )
        self.performance = HistoricalPerformance.objects.create(
            created_by=None,  # Assuming User is nullable
            vendor=self.vendor,
            on_time_delivery_rate=Decimal("99.5"),
            quality_rating_avg=Decimal("4.5"),
            average_response_time=Decimal("48"),
            fulfillment_rate=Decimal("100"),
        )

    def test_historical_performance_serializer(self):
        serializer = HistoricalPerformanceSerializer(instance=self.performance)
        data = serializer.data
        self.assertEqual(data["on_time_delivery_rate"], "99.50")
        self.assertEqual(data["quality_rating_avg"], "4.50")
        self.assertEqual(data["average_response_time"], "48.00")
        self.assertEqual(data["fulfillment_rate"], "100.00")
