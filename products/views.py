from .models import Car
from rest_framework import viewsets
from .serializers import CarSerializer
   

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.filter().order_by('name')
    serializer_class = CarSerializer

class TopCarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.filter(rating__gte=4) 
    serializer_class = CarSerializer
