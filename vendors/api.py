from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HistoricalPerformance, PurchaseOrder, Vendor
from .serializers import (HistoricalPerformanceSerializer,
                          PurchaseOrderSerializer, VendorSerializer)


class VendorListApi(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["name", "vendor_code"]
    search_fields = ["name", "vendor_code", "contact_details"]


class VendorDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]


class VendorPerformanceAPIView(APIView):
    """
    Retrieve performance metrics for a specific vendor.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        vendor = get_object_or_404(Vendor, pk=pk)
        data = {
            "on_time_delivery_rate": vendor.on_time_delivery_rate,
            "quality_rating_avg": vendor.quality_rating_avg,
            "average_response_time": vendor.average_response_time,
            "fulfillment_rate": vendor.fulfillment_rate,
        }
        return Response(data, status=status.HTTP_200_OK)


class PurchaseOrderListApi(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]


class PurchaseOrderDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "po_number"


class HistoricalPerformanceListApi(generics.ListCreateAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    permission_classes = [IsAuthenticated]


class HistoricalPerformanceDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    permission_classes = [IsAuthenticated]
