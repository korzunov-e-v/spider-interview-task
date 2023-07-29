import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()


class ApiClient(APIClient):
    """
    Simple API client with JWT authorization.
    """

    _user: User | None = None
    _access_token: str = ''
    _refresh_token: str = ''
    _token_suffix: str = 'Bearer'

    @property
    def user(self) -> User | None:
        return self._user

    @property
    def access_token(self) -> str:
        return self._access_token

    @property
    def refresh_token(self) -> str:
        return self._refresh_token

    @property
    def token_suffix(self) -> str:
        return self._token_suffix

    def authorize_by_token(self, access_token: str) -> None:
        self.credentials(HTTP_AUTHORIZATION=f'{self._token_suffix} {access_token}')
        self._access_token = access_token

    def authorize(self, active_user: User):
        self.logout()
        refresh_token = RefreshToken.for_user(active_user)

        self._refresh_token = str(refresh_token)
        self._access_token = str(refresh_token.access_token)

        self.authorize_by_token(self.access_token)
        self._user = active_user

        return self


@pytest.fixture
def authorized_api_client(user: User) -> ApiClient:
    return ApiClient().authorize(user)


@pytest.fixture
def admin_authorized_api_client(super_user) -> ApiClient:
    return ApiClient().authorize(super_user)


@pytest.fixture
def anonymous_api_client() -> ApiClient:
    return ApiClient()
