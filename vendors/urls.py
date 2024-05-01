from django.urls import path
from .api import (
    VendorListApi,
    VendorDetailApi,
    VendorPerformanceAPIView,
    PurchaseOrderListApi,
    PurchaseOrderDetailApi,
    HistoricalPerformanceListApi,
    HistoricalPerformanceDetailApi
)

urlpatterns = [
    # URLs for Vendors
    path('vendors/', VendorListApi.as_view(), name='vendor-list'),
    path('vendors/<int:pk>/', VendorDetailApi.as_view(), name='vendor-detail'),
    path('vendors/<int:pk>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),

    # URLs for PurchaseOrders
    path('purchase_orders/', PurchaseOrderListApi.as_view(), name='purchase-order-list'),
    path('purchase_orders/<int:pk>/', PurchaseOrderDetailApi.as_view(), name='purchase-order-detail'),

    # URLs for HistoricalPerformances
    path('historical_performances/', HistoricalPerformanceListApi.as_view(), name='historical-performance-list'),
    path('historical_performances/<int:pk>/', HistoricalPerformanceDetailApi.as_view(), name='historical-performance-detail'),
]
