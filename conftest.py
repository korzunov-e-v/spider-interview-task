from typing import Final

import pytest  # noqa

from api.common.tests.conftest import *  # noqa
from apps.market.tests.conftest import *  # noqa
from apps.organizations.tests.conftest import *  # noqa
from apps.users.tests.conftest import *  # noqa


COUNT_INSTANCES: Final[int] = 5


def pytest_collection_modifyitems(items):
    """Добавлять маркеры автоматически к каждому тесту."""

    for item in items:
        item.add_marker('django_db')


@pytest.fixture
def count_instances() -> int:
    return COUNT_INSTANCES


#
# def get_db_config() -> dict:
#     default_db = settings.DATABASES['default']
#     config = dict(
#         host=default_db['HOST'],
#         port=default_db['PORT'],
#         dbname='postgres',
#         user=default_db['USER'],
#         password=default_db['PASSWORD'],
#     )
#     return config
#
#
# def run_sql(sql, config):
#     conn = psycopg2.connect(**config)
#     conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#     cur = conn.cursor()
#     cur.execute(sql)
#     conn.close()
#
#
# @pytest.fixture(scope='session')
# def django_db_setup(django_db_blocker):
#     from django.conf import settings
#
#     test_database_name = 'test_db'
#     settings.DATABASES['default']['NAME'] = test_database_name
#     db_config = get_db_config()
#
#     run_sql(
#         f'DROP DATABASE IF EXISTS {test_database_name}',
#         config=db_config,
#     )
#     run_sql(
#         f'CREATE DATABASE {test_database_name}',
#         config=db_config,
#     )
#     with django_db_blocker.unblock():
#         call_command('migrate', '--noinput')
#     yield
#     for connection in connections.all():
#         connection.close()
#
#     run_sql(
#         f'DROP DATABASE {test_database_name}',
#         config=db_config,
#     )
