from collections.abc import Callable

import pytest
from django.db import models
from rest_framework import status

from api.common.tests.base_api_test import BaseAPITest
from api.common.tests.urls.organization import (
    get_detail_concern_url,
    get_detail_district_url,
    get_detail_organization_url,
    get_list_concern_url,
    get_list_district_url,
    get_list_organization_url,
)
from api.v1.organizations.tests.conftest import ConcernCRUDFixtures, DistrictCRUDFixtures, OrganizationCRUDFixtures
from apps.organizations.models import Concern, District, Organization


class TestDistrictApi(DistrictCRUDFixtures, BaseAPITest):
    model = District
    get_list_url: Callable = staticmethod(get_list_district_url)
    get_detail_url: Callable = staticmethod(get_detail_district_url)


class TestConcernApi(ConcernCRUDFixtures, BaseAPITest):
    model = Concern
    get_list_url: Callable = staticmethod(get_list_concern_url)
    get_detail_url: Callable = staticmethod(get_detail_concern_url)


class TestOrganizationApi(OrganizationCRUDFixtures, BaseAPITest):
    model = Organization
    get_list_url: Callable = staticmethod(get_list_organization_url)
    get_detail_url: Callable = staticmethod(get_detail_organization_url)

    @pytest.mark.django_db(databases=['default'])
    def test_list(self, authorized_client, anonymous_client, response_as_list_of_dicts: list[dict], district):
        url = self.get_list_url(district.id)

        self._check_inaccessibility(anonymous_client.get, url, status.HTTP_401_UNAUTHORIZED)

        response = authorized_client.get(self.get_list_url(district.id))

        json_data_ordered = self._sort_list_response(response.json())
        expected_ordered = self._sort_list_response(response_as_list_of_dicts)

        assert response.status_code == status.HTTP_200_OK, response.json()
        assert json_data_ordered == expected_ordered

    @pytest.mark.django_db(databases=['default'])
    def test_retrieve(self, authorized_client, anonymous_client, response_as_dict: dict, district):
        instance_id = response_as_dict['id']
        url = self.get_detail_url(instance_id, district.id)

        self._check_inaccessibility(anonymous_client.get, url, status.HTTP_401_UNAUTHORIZED)

        response = authorized_client.get(url)

        json_data = response.json()

        assert response.status_code == status.HTTP_200_OK, response.json()
        assert json_data == response_as_dict

    @pytest.mark.django_db(databases=['default'])
    def test_delete(self, authorized_client, anonymous_client, instance: models.Model, district):
        url = self.get_detail_url(instance.id, district.id)

        self._check_inaccessibility(anonymous_client.delete, url, status.HTTP_401_UNAUTHORIZED)

        response = authorized_client.delete(self.get_detail_url(instance.id, district.id))

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not self.model.objects.all().exists()

    @pytest.mark.django_db(databases=['default'])
    def test_create(self, authorized_client, anonymous_client, instance_as_dict: dict, district):
        instance_as_dict.pop('id')
        url = self.get_list_url(district.id)

        self._check_inaccessibility(anonymous_client.put, url, status.HTTP_401_UNAUTHORIZED)

        response = authorized_client.post(
            url,
            data=instance_as_dict,
            format=self.json_format,
        )

        json_data = response.json()
        instance = self.model.objects.get(pk=json_data.pop('id'))

        assert response.status_code == status.HTTP_201_CREATED, response.json()
        assert json_data == instance_as_dict
        self._compare_data(instance, instance_as_dict)

    @pytest.mark.django_db(databases=['default'])
    def test_change(
        self, authorized_client, anonymous_client, response_as_dict: dict, instance_as_dict: dict, district
    ):
        instance_id = response_as_dict['id']
        url = self.get_detail_url(instance_id, district.id)

        self._check_inaccessibility(anonymous_client.put, url, status.HTTP_401_UNAUTHORIZED)

        response = authorized_client.put(
            url,
            data=instance_as_dict,
            format=self.json_format,
        )

        json_data = response.json()
        instance_as_dict['id'] = instance_id
        instance = self.model.objects.get(pk=instance_id)

        assert response.status_code == status.HTTP_200_OK, response.json()
        assert json_data == instance_as_dict
        self._compare_data(instance, instance_as_dict)

    @pytest.mark.django_db(databases=['default'])
    def test_partial_update(
        self, authorized_client, anonymous_client, response_as_dict: dict, instance_as_dict: dict, district
    ):
        instance_id = response_as_dict['id']
        url = self.get_detail_url(instance_id, district.id)

        self._check_inaccessibility(anonymous_client.patch, url, status.HTTP_401_UNAUTHORIZED)

        response = authorized_client.patch(
            url,
            data=instance_as_dict,
            format=self.json_format,
        )

        json_data = response.json()
        instance_as_dict['id'] = instance_id
        instance = self.model.objects.get(pk=instance_id)

        assert response.status_code == status.HTTP_200_OK, response.json()
        assert json_data == instance_as_dict
        self._compare_data(instance, instance_as_dict)
