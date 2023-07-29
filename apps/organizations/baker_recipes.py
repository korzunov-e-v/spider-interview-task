from model_bakery import seq
from model_bakery.recipe import foreign_key, Recipe

from apps.organizations.models import Concern, District, Organization


district = Recipe(
    District,
    name=seq('Район '),
)

concern = Recipe(
    Concern,
    name=seq('Сеть предприятий '),
)

organization = Recipe(
    Organization,
    name=seq('Предприятие '),
    concern=foreign_key(concern),
)
