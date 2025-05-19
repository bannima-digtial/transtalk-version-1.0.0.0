from django.contrib import admin
from .models import ServiceModel, StatesofCountryModel, DestinationModel, AdvertiseModel

# Register your models here.

admin.site.register(ServiceModel)
admin.site.register(StatesofCountryModel)
admin.site.register(DestinationModel)
admin.site.register(AdvertiseModel)
