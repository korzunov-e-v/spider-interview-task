from datetime import date, datetime

from rest_framework.fields import DateField, DateTimeField


def enforce_datetime(dt: datetime) -> str:
    """
    по хорошему, здесь надо полностью скопировать логику формата из dateTimeField
    в drf, но так тоже работает (пока что)
    """
    return f'{dt.isoformat()}+05:00'


def drf_datetime_format(dt: datetime) -> str:
    return DateTimeField().to_representation(dt)


def drf_date_format(d: date) -> str:
    return DateField().to_representation(d)
