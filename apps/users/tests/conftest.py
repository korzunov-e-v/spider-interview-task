import pytest

from apps.users import baker_recipes


@pytest.fixture
def user():
    return baker_recipes.user.make()


@pytest.fixture
def super_user():
    return baker_recipes.superuser.make()
