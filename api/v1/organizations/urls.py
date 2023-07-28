from rest_framework.routers import SimpleRouter

from api.v1.organizations.views import OrganizationViewSet, DistrictViewSet, ConcernViewSet


router = SimpleRouter()


router.register('districts', DistrictViewSet, basename='districts')
router.register('concerns', ConcernViewSet, basename='concerns')
router.register('(?P<district>[^/.]+)', OrganizationViewSet, basename='organizations')

urlpatterns = router.urls
