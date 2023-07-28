from django.contrib import admin
from apps.market.models import Product, Category


admin.site.register(Product)
admin.site.register(Category)
