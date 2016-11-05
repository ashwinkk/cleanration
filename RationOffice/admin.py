from django.contrib import admin

# Register your models here.

from .models import RationOffice,RationOfficer

class RationOfficeAdmin(admin.ModelAdmin):
	list_display = ["id","Location","NumberOfRationShops"]
	class Meta:
		model = RationOffice

class RationOfficerAdmin(admin.ModelAdmin):
	list_display = ["Username","Office","FullName"]
	class Meta:
		model = RationOfficer

admin.site.register(RationOffice,RationOfficeAdmin)
admin.site.register(RationOfficer,RationOfficerAdmin)


