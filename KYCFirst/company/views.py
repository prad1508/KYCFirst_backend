from rest_framework import viewsets
from company.serializers import CompanySerializer, LocationSerializer
from company.models import Company, Location
from rest_framework.permissions import IsAuthenticated
from agent.permissions import AdminReadOnly


class CompanyApi(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    #permission_classes=[AdminReadOnly]
    
class LocationApi(viewsets.ModelViewSet):
    queryset=Location.objects.all()
    serializer_class=LocationSerializer
    #permission_classes=[AdminReadOnly]