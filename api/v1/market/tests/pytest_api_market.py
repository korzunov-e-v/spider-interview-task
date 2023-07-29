from collections.abc import Callable

from api.common.tests.base_api_test import BaseAPITest
from api.common.tests.urls.market import (
    get_detail_category_url,
    get_detail_product_url,
    get_list_category_url,
    get_list_product_url,
)
from api.v1.market.tests.conftest import CategoryCRUDFixtures, ProductCRUDFixtures
from apps.market.models import Category, Product


class TestCategoryApi(CategoryCRUDFixtures, BaseAPITest):
    model = Category
    get_list_url: Callable = staticmethod(get_list_category_url)
    get_detail_url: Callable = staticmethod(get_detail_category_url)


class TestProductApi(ProductCRUDFixtures, BaseAPITest):
    model = Product
    get_list_url: Callable = staticmethod(get_list_product_url)
    get_detail_url: Callable = staticmethod(get_detail_product_url)
