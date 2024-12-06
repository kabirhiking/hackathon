
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import (
    HealthData, HealthTip, MentalHealthCheckIn
)
from .serializers import (
    HealthDataSerializer, HealthTipSerializer, MentalHealthCheckInSerializer
    
)


class HealthDataViewSet(viewsets.ModelViewSet):
    queryset = HealthData.objects.all()
    serializer_class = HealthDataSerializer
    # permission_classes = [IsAuthenticated]


class HealthTipViewSet(viewsets.ModelViewSet):
    queryset = HealthTip.objects.all()
    serializer_class = HealthTipSerializer
    # permission_classes = [IsAuthenticated]


class MentalHealthCheckInViewSet(viewsets.ModelViewSet):
    queryset = MentalHealthCheckIn.objects.all()
    serializer_class = MentalHealthCheckInSerializer
    # permission_classes = [IsAuthenticated]

