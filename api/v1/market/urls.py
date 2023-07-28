from rest_framework.routers import SimpleRouter

from api.v1.market.views import CategoryViewSet, ProductViewSet


router = SimpleRouter()

router.register('category', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')

urlpatterns = router.urls
