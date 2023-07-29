from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet

from api.v1.organizations.serializers import ConcernSerializer, DistrictSerializer, OrganizationSerializer
from apps.organizations.models import Concern, District, Organization


class OrganizationViewSet(ModelViewSet):
    def get_queryset(self):
        return Organization.objects.filter(district=self.kwargs['district'])

    serializer_class = OrganizationSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'concern', 'district', 'products__category']


class ConcernViewSet(ModelViewSet):
    queryset = Concern.objects.all()
    serializer_class = ConcernSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['id', 'name']


class DistrictViewSet(ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['id', 'name']
