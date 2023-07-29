import pytest

from apps.market import baker_recipes
from apps.market.models import Category, Product


@pytest.fixture
def categorys(count_instances) -> tuple[Category]:
    return baker_recipes.category.make(_quantity=count_instances)


@pytest.fixture
def category() -> Category:
    return baker_recipes.category.make()


@pytest.fixture
def category_uncommitted_instance() -> Category:
    return baker_recipes.category.prepare(_save_related=True)


@pytest.fixture
def products(count_instances) -> tuple[Product]:
    return baker_recipes.product.make(_quantity=count_instances)


@pytest.fixture
def product() -> Product:
    return baker_recipes.product.make()


@pytest.fixture
def product_uncommitted_instance() -> Product:
    return baker_recipes.product.prepare(_save_related=True)
