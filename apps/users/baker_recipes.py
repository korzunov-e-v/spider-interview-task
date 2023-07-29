from django.contrib.auth import get_user_model
from model_bakery import seq
from model_bakery.recipe import Recipe


User = get_user_model()


user = Recipe(
    User,
    username=seq('username'),
    email=seq('user', suffix='@example.com'),
    is_active=True,
)


superuser = user.extend(
    is_superuser=True,
    email=seq('admin', suffix='@example.com'),
)
