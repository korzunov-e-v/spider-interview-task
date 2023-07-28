from django.urls import include, path


urlpatterns = [
    # path('users/', include('api.v1.users.urls')),
    path('market/', include('api.v1.market.urls')),
    path('organizations/', include('api.v1.organizations.urls')),
]
