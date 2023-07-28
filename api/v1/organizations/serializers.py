from rest_framework import serializers

from apps.organizations.models import Organization, Concern, District


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'id',
            'name',
            'concern',
            'district',
        )


class ConcernSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concern
        fields = (
            'id',
            'name',
        )


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = (
            'id',
            'name',
        )
