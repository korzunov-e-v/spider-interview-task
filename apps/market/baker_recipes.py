from model_bakery import seq
from model_bakery.recipe import foreign_key, Recipe

from apps.market.models import Category, Product
from apps.organizations.baker_recipes import organization


category = Recipe(
    Category,
    name=seq('Категория '),
)

product = Recipe(
    Product, name=seq('Продукт '), price=seq(''), category=foreign_key(category), organization=foreign_key(organization)
)
