# 

from rest_framework import serializers
from .models import (
    CustomUser, HealthData, HealthTip, MentalHealthCheckIn
)

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_doctor', 'phone', 'address']


class HealthDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthData
        fields = '__all__'


class HealthTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthTip
        fields = '__all__'


class MentalHealthCheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentalHealthCheckIn
        fields = '__all__'

