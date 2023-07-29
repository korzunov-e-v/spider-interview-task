from rest_framework.reverse import reverse


def get_list_district_url() -> str:
    return reverse('districts-list')


def get_detail_district_url(pk: int) -> str:
    return reverse('districts-detail', kwargs={'pk': pk})


def get_list_concern_url() -> str:
    return reverse('concerns-list')


def get_detail_concern_url(pk: int) -> str:
    return reverse('concerns-detail', kwargs={'pk': pk})


def get_list_organization_url(district: int) -> str:
    return reverse('organizations-list', kwargs={'district': district})


def get_detail_organization_url(pk: int, district: int) -> str:
    return reverse('organizations-detail', kwargs={'pk': pk, 'district': district})
