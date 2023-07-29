from django.contrib import admin

from apps.organizations.models import Concern, District, Organization


admin.site.register(Concern)
admin.site.register(Organization)
admin.site.register(District)
