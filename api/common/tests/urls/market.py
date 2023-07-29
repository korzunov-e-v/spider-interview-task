from rest_framework.reverse import reverse


def get_list_category_url() -> str:
    return reverse('category-list')


def get_detail_category_url(pk: int) -> str:
    return reverse('category-detail', kwargs={'pk': pk})


def get_list_product_url() -> str:
    return reverse('product-list')


def get_detail_product_url(pk: int) -> str:
    return reverse('product-detail', kwargs={'pk': pk})
