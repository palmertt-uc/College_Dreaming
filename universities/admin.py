from django.contrib import admin
from .models import Institutions, Cities, Zipcodes, Admissions, Completionrates, Costs, Institutiontypes, Majors, \
    Programs, Undergraduates


class RelationInstitutions(admin.ModelAdmin):
    raw_id_fields = ('zipcodeid',)


# Register your models here.
admin.site.register(Institutions, RelationInstitutions)
admin.site.register(Cities)
admin.site.register(Zipcodes)
admin.site.register(Admissions)
admin.site.register(Completionrates)
admin.site.register(Costs)
admin.site.register(Institutiontypes)
admin.site.register(Majors)
admin.site.register(Programs)
admin.site.register(Undergraduates)
