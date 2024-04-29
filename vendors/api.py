from rest_framework.decorators import api_view, schema


from rest_framework.response import Response
from .models import Vendor
from .serializers import VendorSerializer


@api_view(['GET'])
def vendor_list_api(request):
    vendors = Vendor.objects.all()
    data = VendorSerializer(vendors, many=True).data
    return Response({'data': data})

