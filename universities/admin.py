from django.contrib import admin
from .models import Institutions, Cities, Zipcodes, Admissions, Completionrates, Costs, Institutiontypes, Majors, \
    Programs, Undergraduates, Earnings, Crime, Climate


class RelationInstitutions(admin.ModelAdmin):
    raw_id_fields = ('zipcodeid',)
    search_fields = ('instname',)


class RelationCities(admin.ModelAdmin):
    search_fields = ('city', 'state')


class RelationUndergraduates(admin.ModelAdmin):
    search_fields = ('institutionid__instname',)


# Register your models here.
admin.site.register(Institutions, RelationInstitutions)
admin.site.register(Cities, RelationCities)
admin.site.register(Zipcodes)
admin.site.register(Admissions)
admin.site.register(Completionrates)
admin.site.register(Costs)
admin.site.register(Institutiontypes)
admin.site.register(Majors)
admin.site.register(Programs)
admin.site.register(Undergraduates, RelationUndergraduates)
admin.site.register(Earnings)
admin.site.register(Crime)
admin.site.register(Climate)
