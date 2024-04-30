from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Vendor
from .serializers import VendorSerializer
from rest_framework import status, generics, filters
from django_filters.rest_framework import DjangoFilterBackend


# @api_view(['GET', 'POST'])
# def vendor_list_api(request):
#     if request.method == 'GET':
#         vendors = Vendor.objects.all()
#         serializer = VendorSerializer(vendors, many=True)
#         return Response({'data': serializer.data})
#     elif request.method == 'POST':
#         serializer = VendorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def vendor_detail_api(request, id=None):
#     vendor = get_object_or_404(Vendor, id=id)
#     if request.method == 'GET':
#         serializer = VendorSerializer(vendor)
#         return Response({'data': serializer.data})
#     elif request.method in ['PUT', 'PATCH']:
#         serializer = VendorSerializer(vendor, data=request.data, partial=(request.method == 'PATCH'))
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         vendor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['PUT', 'DELETE'])
# def vendor_modify_api(request, id):
#     vendor = get_object_or_404(Vendor, id=id)
#     if request.method == 'PUT':
#         serializer = VendorSerializer(vendor, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         vendor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class VendorListApi(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'vendor_code', 'quality_rating_avg']
    search_fields = ['name', 'vendor_code', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']


class VendorDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer