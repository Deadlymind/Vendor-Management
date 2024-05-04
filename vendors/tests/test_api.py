from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from vendors.models import Vendor, PurchaseOrder, HistoricalPerformance
from decimal import Decimal
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken


class BaseTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # create a user and generate a JWT for them
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
            )
        cls.token = RefreshToken.for_user(cls.user)

    def setUp(self):
        # authenticate using the token
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')


class VendorAPITestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.vendor = Vendor.objects.create(
            name="Test Vendor",
            contact_details="1234567890",
            address="123 Test St",
            vendor_code="V001",
        )

    def test_vendor_list(self):
        url = reverse("vendor-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Test Vendor")

    def test_vendor_detail(self):
        url = reverse("vendor-detail", kwargs={'pk': self.vendor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Vendor")


class PurchaseOrderAPITestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.vendor = Vendor.objects.create(
            name="Test Vendor",
            contact_details="1234567890",
            address="123 Test St",
            vendor_code="V001",
        )
        self.purchase_order = PurchaseOrder.objects.create(
            vendor=self.vendor,
            order_date=timezone.now(),
            delivery_date=timezone.now() + timezone.timedelta(days=4),
            items={"item1": "test item"},
            quantity=10,
            status="Pending",
            quality_rating=Decimal("4.0"),
            response_time=Decimal("24"),
            on_time_delivery=True,
        )

    def test_purchase_order_list(self):
        url = reverse("purchase-order-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_purchase_order_detail(self):
        url = reverse(
            "purchase-order-detail",
            kwargs={'po_number': self.purchase_order.po_number})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class HistoricalPerformanceAPITestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.vendor = Vendor.objects.create(
            name="Test Vendor", vendor_code="V123"
        )
        self.performance = HistoricalPerformance.objects.create(
            vendor=self.vendor,
            on_time_delivery_rate=Decimal("99.5"),
            quality_rating_avg=Decimal("4.5"),
            average_response_time=Decimal("48"),
            fulfillment_rate=Decimal("100"),
        )

    def test_historical_performance_list(self):
        url = reverse("historical-performance-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_historical_performance_detail(self):
        url = reverse(
            "historical-performance-detail",
            kwargs={'pk': self.performance.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
