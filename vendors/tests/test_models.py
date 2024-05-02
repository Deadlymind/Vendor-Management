from django.test import TestCase
from vendors.models import Vendor, PurchaseOrder, HistoricalPerformance
from django.utils import timezone
from datetime import timedelta

class VendorModelTest(TestCase):
    def setUp(self):
        # Setup run before every test method.
        self.vendor = Vendor.objects.create(
            name="Test Vendor",
            contact_details="1234567890",
            address="123 Test St, Test City",
            vendor_code="V001",
            on_time_delivery_rate=99.5,
            quality_rating_avg=4.8,
            average_response_time=24.0,
            fulfillment_rate=95.0
        )

    def test_string_representation(self):
        # Test the string representation of the model.
        self.assertEqual(str(self.vendor), self.vendor.name)

    def test_vendor_fields(self):
        # Test that each field contains the correct data.
        self.assertEqual(self.vendor.contact_details, "1234567890")
        self.assertEqual(self.vendor.address, "123 Test St, Test City")
        self.assertEqual(self.vendor.vendor_code, "V001")
        self.assertAlmostEqual(self.vendor.on_time_delivery_rate, 99.5)
        self.assertAlmostEqual(self.vendor.quality_rating_avg, 4.8)
        self.assertAlmostEqual(self.vendor.average_response_time, 24.0)
        self.assertAlmostEqual(self.vendor.fulfillment_rate, 95.0)

    def test_field_labels(self):
        # Test label for a specific field.
        field_label = self.vendor._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')


class PurchaseOrderModelTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        Vendor.objects.create(
            name="Sample Vendor",
            contact_details="987654321",
            address="456 Test Lane, Testville",
            vendor_code="V002"
        )
        self.purchase_order = PurchaseOrder.objects.create(
            po_number="PO123456",
            vendor=Vendor.objects.get(vendor_code="V002"),
            order_date=timezone.now(),
            delivery_date=timezone.now() + timedelta(days=5),
            items={"item1": "Test item", "qty": 10},
            quantity=10,
            status="Pending"
        )

    def test_po_creation(self):
        # Test that the purchase order is created correctly.
        self.assertTrue(isinstance(self.purchase_order, PurchaseOrder))
        self.assertEqual(self.purchase_order.__str__(), self.purchase_order.po_number)

    def test_po_fields(self):
        # Test specific fields for correct values
        self.assertEqual(self.purchase_order.quantity, 10)
        self.assertEqual(self.purchase_order.status, "Pending")

    def test_po_date_logic(self):
        # Test the logic applied to dates
        self.assertFalse(self.purchase_order.delivery_date < self.purchase_order.order_date)


class HistoricalPerformanceModelTest(TestCase):
    def setUp(self):
        # Creating a Vendor to link to HistoricalPerformance
        self.vendor = Vendor.objects.create(
            name="Historical Vendor",
            contact_details="123456789",
            address="789 History St, Pastville",
            vendor_code="V003"
        )
        self.performance = HistoricalPerformance.objects.create(
            vendor=self.vendor,
            on_time_delivery_rate=88.5,
            quality_rating_avg=3.5,
            average_response_time=48.0,
            fulfillment_rate=75.0
        )

    def test_historical_performance_creation(self):
        # Test the creation of the HistoricalPerformance record
        self.assertTrue(isinstance(self.performance, HistoricalPerformance))
        self.assertEqual(self.performance.__str__(), self.vendor.name)

    def test_performance_fields(self):
        # Ensure that all performance metrics are stored correctly
        self.assertAlmostEqual(self.performance.on_time_delivery_rate, 88.5)
        self.assertAlmostEqual(self.performance.quality_rating_avg, 3.5)
        self.assertAlmostEqual(self.performance.average_response_time, 48.0)
        self.assertAlmostEqual(self.performance.fulfillment_rate, 75.0)

