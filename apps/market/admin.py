from django.contrib import admin

from apps.market.models import Category, Product


admin.site.register(Product)
admin.site.register(Category)
