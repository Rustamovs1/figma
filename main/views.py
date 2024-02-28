from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from .models import *
from .serializer import *


@api_view(['GET'])
def get_banner(request):
    banner = Banner.objects.all().order_by('-id')[:3]
    ser_data = BannerSerializer(banner, many=True).data
    return Response(ser_data)