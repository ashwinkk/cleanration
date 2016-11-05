from django.contrib import admin

# Register your models here.

from .models import Customer,Item,RationShop,ShopKeeper


class CustomerAdmin(admin.ModelAdmin):
	list_display = ["RationCardNumber","Fullname","CardType","LastSentOTP",
	"PhoneNumber","WheatBalance","RiceBalance",
	"SugarBalance","KeroseneBalance"
	]
	
	class Meta:
		model = Customer

class ShopKeeperAdmin(admin.ModelAdmin):
	list_display = ["Shop","Fullname","Username"]
	
	class Meta:
		model = ShopKeeper

class ItemsAdmin(admin.ModelAdmin):
	list_display = ["item_name","price_APL","limit_APL","price_BPL","limit_BPL"]
	class Meta:
		model = Item

class RationShopAdmin(admin.ModelAdmin):
	list_display = ["id","Office","Location","NumberOfBPLCostumers",
	"NumberOfAPLCostumers","WheatBalance","RiceBalance",
	"SugarBalance","KeroseneBalance"]
	class Meta:
		model = RationShop

admin.site.register(RationShop,RationShopAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Item,ItemsAdmin)
admin.site.register(ShopKeeper,ShopKeeperAdmin)
