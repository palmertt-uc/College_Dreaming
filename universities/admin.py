from django.contrib import admin
from .models import Institutions, Cities, Zipcodes

# Register your models here.
admin.site.register(Institutions)
admin.site.register(Cities)
admin.site.register(Zipcodes)