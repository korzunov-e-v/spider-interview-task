from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet

from api.v1.market.serializers import CategorySerializer, ProductSerializer
from apps.market.models import Category, Product


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['id', 'name']


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'price', 'category', 'organization']
