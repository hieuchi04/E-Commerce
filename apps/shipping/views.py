from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Shipping
from .serializers import ShippingSerializer

# Create your views here.



class GetShippingView(APIView):
    def get(self, request, format=None):
        try:
            shipping = Shipping.objects.all().order_by('price')
            shipping = ShippingSerializer(shipping, many=True)
            return Response({'shipping': shipping.data}, status=status.HTTP_200_OK)
            
        except Shipping.DoesNotExist:
            return Response({'error': 'Shipping not found'}, status=status.HTTP_404_NOT_FOUND) 