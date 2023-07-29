import pytest

from apps.market.models import Category, Product


class CategoryCRUDFixtures:
    @pytest.fixture()
    def response_as_list_of_dicts(self, categorys) -> list[dict]:
        return [self._make_dict_from_instance(category) for category in categorys]

    @pytest.fixture()
    def response_as_dict(self, response_as_list_of_dicts: list[dict]) -> dict:
        return response_as_list_of_dicts[0]

    @pytest.fixture()
    def instance(self, category) -> Category:
        return category

    @pytest.fixture()
    def instance_as_dict(self, category_uncommitted_instance) -> dict:
        return self._make_dict_from_instance(category_uncommitted_instance)

    @staticmethod
    def _make_dict_from_instance(category: Category) -> dict:
        return {
            'id': category.id,
            'name': category.name,
        }


class ProductCRUDFixtures:
    @pytest.fixture()
    def response_as_list_of_dicts(self, products) -> list[dict]:
        return [self._make_dict_from_instance(product) for product in products]

    @pytest.fixture()
    def response_as_dict(self, response_as_list_of_dicts: list[dict]) -> dict:
        return response_as_list_of_dicts[0]

    @pytest.fixture()
    def instance(self, product) -> Product:
        return product

    @pytest.fixture()
    def instance_as_dict(self, product_uncommitted_instance) -> dict:
        return self._make_dict_from_instance(product_uncommitted_instance)

    @staticmethod
    def _make_dict_from_instance(product: Product) -> dict:
        return {
            'id': product.id,
            'name': product.name,
            'price': f'{float(product.price):.2f}',
            'category': product.category_id,
            'organization': product.organization_id,
        }
