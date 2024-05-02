from decimal import Decimal
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils import timezone
from vendors.models import Vendor, PurchaseOrder, HistoricalPerformance
from django.contrib.auth.models import User

class VendorAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.vendor = Vendor.objects.create(
            name="Test Vendor",
            contact_details="1234567890",
            address="123 Test St",
            vendor_code="V001"
        )

    def test_vendor_list(self):
        url = reverse('vendor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_vendor_detail(self):
        url = reverse('vendor-detail', kwargs={'pk': self.vendor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.vendor.name)

class PurchaseOrderAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.vendor = Vendor.objects.create(
            name="Test Vendor",
            contact_details="1234567890",
            address="123 Test St",
            vendor_code="V001"
        )
        order_date = timezone.make_aware(timezone.datetime(2024, 1, 1))
        delivery_date = timezone.make_aware(timezone.datetime(2024, 1, 5))
        issue_date = timezone.make_aware(timezone.datetime(2024, 1, 1))
        acknowledgment_date = timezone.make_aware(timezone.datetime(2024, 1, 2))
        self.purchase_order = PurchaseOrder.objects.create(
            vendor=self.vendor,
            order_date=order_date,
            delivery_date=delivery_date,
            items={"item1": "test item"},
            quantity=10,
            status="Pending",
            quality_rating=Decimal('4.0'),
            issue_date=issue_date,
            acknowledgment_date=acknowledgment_date,
            response_time=Decimal('24'),
            on_time_delivery=True
        )

    def test_purchase_order_list(self):
        url = reverse('purchase-order-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_purchase_order_detail(self):
        url = reverse('purchase-order-detail', kwargs={'po_number': self.purchase_order.po_number})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class HistoricalPerformanceAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.vendor = Vendor.objects.create(
            name="Test Vendor",
            vendor_code="V123"
        )
        self.performance = HistoricalPerformance.objects.create(
            vendor=self.vendor,
            on_time_delivery_rate=Decimal('99.5'),
            quality_rating_avg=Decimal('4.5'),
            average_response_time=Decimal('48'),
            fulfillment_rate=Decimal('100')
        )

    def test_historical_performance_list(self):
        url = reverse('historical-performance-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_historical_performance_detail(self):
        url = reverse('historical-performance-detail', kwargs={'pk': self.performance.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
