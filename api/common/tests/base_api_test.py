from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Final

import pytest
from django.db import models
from rest_framework import status

from api.common.tests.conftest import ApiClient


class BaseAPITest(ABC):
    json_format: Final[str] = 'json'
    model: type[models.Model]
    list_sorting_field: str = 'id'

    @abstractmethod
    def response_as_list_of_dicts(self, response_as_list_of_dicts: list[dict]) -> list[dict]:
        """Fixture."""

    @abstractmethod
    def response_as_dict(self, response_as_dict: dict) -> dict:
        """Fixture."""

    @abstractmethod
    def instance(self, instance: models.Model) -> models.Model:
        """Fixture."""

    @abstractmethod
    def instance_as_dict(self, instance_as_dict: dict) -> dict:
        """Fixture."""

    @pytest.fixture
    def authorized_client(self, authorized_api_client: ApiClient) -> ApiClient:
        return authorized_api_client

    @pytest.fixture
    def anonymous_client(self, anonymous_api_client) -> ApiClient:
        return anonymous_api_client

    @abstractmethod
    def get_list_url(self) -> str:
        ...

    @abstractmethod
    def get_detail_url(self, *args, **kwargs) -> str:
        ...

    @abstractmethod
    def _make_dict_from_instance(self, instance: models.Model) -> dict:
        ...

    @pytest.mark.django_db(databases=['default'])
    def test_list(self, authorized_client, anonymous_client, response_as_list_of_dicts: list[dict]):
        url = self.get_list_url()

        self._check_inaccessibility(anonymous_client.get, url, status.HTTP_401_UNAUTHORIZED)

        response = authorized_client.get(self.get_list_url())

        json_data_ordered = self._sort_list_response(response.json())
        expected_ordered = self._sort_list_response(response_as_list_of_dicts)

        assert response.status_code == status.HTTP_200_OK, response.json()
        assert json_data_ordered == expected_ordered

    @pytest.mark.django_db(databases=['default'])
    def test_retrieve(self, authorized_client, anonymous_client, response_as_dict: dict):
        instance_id = response_as_dict['id']
        url = self.get_detail_url(instance_id)

        self._check_inaccessibility(anonymous_client.get, url, status.HTTP_401_UNAUTHORIZED)

        response = authorized_client.get(url)

        json_data = response.json()

        assert response.status_code == status.HTTP_200_OK, response.json()
        assert json_data == response_as_dict

    @pytest.mark.django_db(databases=['default'])
    def test_delete(self, authorized_client, anonymous_client, instance: models.Model):
        url = self.get_detail_url(instance.id)

        self._check_inaccessibility(anonymous_client.delete, url, status.HTTP_401_UNAUTHORIZED)

        response = authorized_client.delete(self.get_detail_url(instance.id))

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not self.model.objects.all().exists()

    @pytest.mark.django_db(databases=['default'])
    def test_create(self, authorized_client, anonymous_client, instance_as_dict: dict):
        instance_as_dict.pop('id')
        url = self.get_list_url()

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
    def test_change(self, authorized_client, anonymous_client, response_as_dict: dict, instance_as_dict: dict):
        instance_id = response_as_dict['id']
        url = self.get_detail_url(instance_id)

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
    def test_partial_update(self, authorized_client, anonymous_client, response_as_dict: dict, instance_as_dict: dict):
        instance_id = response_as_dict['id']
        url = self.get_detail_url(instance_id)

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

    def _check_inaccessibility(self, client_method: Callable, url: str, http_status: int) -> None:
        response = client_method(url, data={}, format=self.json_format)
        assert response.status_code == http_status

    def _compare_data(self, instance: models.Model, request_data: dict) -> None:
        instance_as_dict = self._make_dict_from_instance(instance)
        for field_name, value in request_data.items():
            assert instance_as_dict[field_name] == value

    def _sort_list_response(self, list_response: list[dict]) -> list[dict]:
        sorted_sequence = sorted(list_response, key=lambda record: record[self.list_sorting_field])
        return list(sorted_sequence)
