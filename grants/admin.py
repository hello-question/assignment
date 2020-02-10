from django.contrib import admin
from .models import Housing, Household, FamilyMember, Gender, MaritalStatus, \
    OccupationType

# Register your models here.
admin.site.register(Housing)
admin.site.register(Household)
admin.site.register(FamilyMember)
admin.site.register(Gender)
admin.site.register(MaritalStatus)
admin.site.register(OccupationType)
