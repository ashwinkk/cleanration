from django.contrib import admin

from .models import Approved
# Register your models here.

class AdminApproval(admin.ModelAdmin):
    list_display=["RationShop","Status"]

    class Meta:
        model = Approved

admin.site.register(Approved,AdminApproval)
