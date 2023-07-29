import pytest

from apps.organizations import baker_recipes
from apps.organizations.models import Concern, District, Organization


@pytest.fixture
def districts(count_instances) -> tuple[District]:
    return baker_recipes.district.make(_quantity=count_instances)


@pytest.fixture
def district() -> District:
    return baker_recipes.district.make()


@pytest.fixture
def district_uncommitted_instance() -> District:
    return baker_recipes.district.prepare(_save_related=True)


@pytest.fixture
def concerns(count_instances) -> tuple[Concern]:
    return baker_recipes.concern.make(_quantity=count_instances)


@pytest.fixture
def concern() -> Concern:
    return baker_recipes.concern.make()


@pytest.fixture
def concern_uncommitted_instance() -> Concern:
    return baker_recipes.concern.prepare(_save_related=True)


@pytest.fixture
def organizations(count_instances, district) -> tuple[Organization]:
    return baker_recipes.organization.make(_quantity=count_instances, district=[district])


@pytest.fixture
def organization(district) -> Organization:
    return baker_recipes.organization.make(district=[district])


@pytest.fixture
def organization_uncommitted_instance(district) -> Organization:
    return baker_recipes.organization.prepare(_save_related=True)
