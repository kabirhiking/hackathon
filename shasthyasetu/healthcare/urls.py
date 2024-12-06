# from django.urls import path,include 
# from rest_framework.routers import DefaultRouter
# from .views import CustomUserViewSet, HealthDataViewSet,HealthTokenViewSet, AppointmentViewSet 
# from .views import WellnessPlanView

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HealthDataViewSet, HealthTipViewSet, MentalHealthCheckInViewSet
)

router = DefaultRouter()
router.register(r'health-data', HealthDataViewSet)
router.register(r'health-tips', HealthTipViewSet)
router.register(r'mental-health-checkin', MentalHealthCheckInViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


