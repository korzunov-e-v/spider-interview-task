import pytest

from apps.organizations.models import Concern, District, Organization


class DistrictCRUDFixtures:
    @pytest.fixture()
    def response_as_list_of_dicts(self, districts) -> list[dict]:
        return [self._make_dict_from_instance(district) for district in districts]

    @pytest.fixture()
    def response_as_dict(self, response_as_list_of_dicts: list[dict]) -> dict:
        return response_as_list_of_dicts[0]

    @pytest.fixture()
    def instance(self, district) -> District:
        return district

    @pytest.fixture()
    def instance_as_dict(self, district_uncommitted_instance) -> dict:
        return self._make_dict_from_instance(district_uncommitted_instance)

    @staticmethod
    def _make_dict_from_instance(district: District) -> dict:
        return {
            'id': district.id,
            'name': district.name,
        }


class ConcernCRUDFixtures:
    @pytest.fixture()
    def response_as_list_of_dicts(self, concerns) -> list[dict]:
        return [self._make_dict_from_instance(concern) for concern in concerns]

    @pytest.fixture()
    def response_as_dict(self, response_as_list_of_dicts: list[dict]) -> dict:
        return response_as_list_of_dicts[0]

    @pytest.fixture()
    def instance(self, concern) -> Concern:
        return concern

    @pytest.fixture()
    def instance_as_dict(self, concern_uncommitted_instance) -> dict:
        return self._make_dict_from_instance(concern_uncommitted_instance)

    @staticmethod
    def _make_dict_from_instance(concern: Concern) -> dict:
        return {
            'id': concern.id,
            'name': concern.name,
        }


class OrganizationCRUDFixtures:
    @pytest.fixture()
    def response_as_list_of_dicts(self, organizations) -> list[dict]:
        return [self._make_dict_from_instance(organization) for organization in organizations]

    @pytest.fixture()
    def response_as_dict(self, response_as_list_of_dicts: list[dict]) -> dict:
        return response_as_list_of_dicts[0]

    @pytest.fixture()
    def instance(self, organization) -> Organization:
        return organization

    @pytest.fixture()
    def instance_as_dict(self, organization_uncommitted_instance, district) -> dict:
        return self._make_special_dict_from_instance(organization_uncommitted_instance, district)

    @staticmethod
    def _make_dict_from_instance(organization: Organization) -> dict:
        return {
            'id': organization.id,
            'name': organization.name,
            'concern': organization.concern_id,
            'district': [dis.id for dis in organization.district.all()],
        }

    @staticmethod
    def _make_special_dict_from_instance(organization: Organization, district: District) -> dict:
        return {
            'id': organization.id,
            'name': organization.name,
            'concern': organization.concern_id,
            'district': [district.id],
        }
