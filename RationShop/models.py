from __future__ import unicode_literals

from django.db import models

# Create your models here.

from RationOffice.models import RationOffice as Office

class Item(models.Model):
	item_name = models.CharField(max_length=10)
	price_APL = models.FloatField(default=0.0)
	price_BPL = models.FloatField(default=0.0)
	limit_APL = models.FloatField(default=0.0)
	limit_BPL = models.FloatField(default=0.0)


def findLimits():
	global wheat_apl_limit ,wheat_bpl_limit ,rice_apl_limit ,rice_bpl_limit ,sugar_apl_limit,sugar_bpl_limit,kerosene_apl_limit,kerosene_bpl_limit

	wheat_apl_limit = Item.objects.get(item_name='Wheat').limit_APL
	wheat_bpl_limit = Item.objects.get(item_name='Wheat').limit_BPL
	rice_apl_limit = Item.objects.get(item_name='Rice').limit_APL
	rice_bpl_limit = Item.objects.get(item_name='Rice').limit_BPL
	sugar_apl_limit = Item.objects.get(item_name='Sugar').limit_APL
	sugar_bpl_limit = Item.objects.get(item_name='Sugar').limit_BPL
	kerosene_apl_limit = Item.objects.get(item_name='Kerosene').limit_APL
	kerosene_bpl_limit = Item.objects.get(item_name='Kerosene').limit_BPL

findLimits()

class RationShop(models.Model):
	Location = models.CharField(max_length=50)
	Office = models.ForeignKey(Office,on_delete=models.CASCADE)
	NumberOfBPLCostumers = models.PositiveSmallIntegerField(default=0)
	NumberOfAPLCostumers = models.PositiveSmallIntegerField(default=0)

	WheatBalance = models.FloatField(default=0.0)
	RiceBalance = models.FloatField(default=0.0)
	SugarBalance = models.FloatField(default=0.0)
	KeroseneBalance = models.FloatField(default=0.0)

	def __str__(self):
		return 'ID: %d,Loc: %s'%(self.id,self.Location)


	def allocate(self):
		nAPL = self.NumberOfAPLCostumers
		nBPL = self.NumberOfBPLCostumers
		self.WheatBalance = self.nAPL*wheat_apl_limit + self.nBPL*wheat_bpl_limit
		self.RiceBalance = self.nAPL*rice_apl_limit + self.nBPL*rice_bpl_limit
		self.SugarBalance = self.nAPL*sugar_apl_limit + self.nBPL*sugar_bpl_limit
		self.KeroseneBalance = self.nAPL*kerosene_apl_limit + self.nBPL*kerosene_bpl_limit
		
		self.save()


class Customer(models.Model):

	Fullname = models.CharField(max_length=20)
	CardType = models.CharField(default='APL',max_length=3)
	Verified = models.BooleanField(default=False)
	RationCardNumber = models.CharField(max_length=20,primary_key=True)
	PhoneNumber = models.CharField(max_length=15)
	LastSentOTP = models.PositiveIntegerField(null=True,blank=True)

	WheatBalance = models.FloatField(default=0.0)
	RiceBalance = models.FloatField(default=0.0)
	SugarBalance = models.FloatField(default=0.0)
	KeroseneBalance = models.FloatField(default=0.0)

	Shop =  models.ForeignKey(RationShop,on_delete=models.CASCADE)


	def allocate(self):
		if self.CardType=='APL':
			self.WheatBalance = wheat_apl_limit
			self.RiceBalance = rice_apl_limit
			self.SugarBalance = sugar_apl_limit
			self.KeroseneBalance = kerosene_apl_limit
		else:
			self.WheatBalance = wheat_bpl_limit
			self.RiceBalance = rice_bpl_limit
			self.SugarBalance = sugar_bpl_limit
			self.KeroseneBalance = kerosene_bpl_limit
		self.save()


	def balance(self):
		return {
			'Wheat'  : self.WheatBalance,
			'Rice' : self.RiceBalance,
			'Sugar' : self.SugarBalance,
			'Kerosene' : self.KeroseneBalance,
			'Wheat-Shop'  : self.Shop.WheatBalance,
			'Rice-Shop' : self.Shop.RiceBalance,
			'Sugar-Shop' : self.Shop.SugarBalance,
			'Kerosene-Shop' : self.Shop.KeroseneBalance,
		}

	def purchase(self,itemlist):
		if itemlist['Wheat'] <= self.WheatBalance and itemlist['Rice'] <= self.RiceBalance and itemlist['Sugar'] <= self.SugarBalance and itemlist['Kerosene'] <= self.KeroseneBalance:
			
			price = 0
			for item in ['Wheat','Rice','Sugar','Kerosene']:
				if self.CardType=='APL':
					price += Item.objects.get(item_name=item).price_APL*itemlist[item]
				else:
					price += Item.objects.get(item_name=item).price_BPL*itemlist[item]

			self.WheatBalance -= itemlist['Wheat']
			self.RiceBalance -= itemlist['Rice']
			self.SugarBalance -= itemlist['Sugar']
			self.KeroseneBalance -= itemlist['Kerosene']

			self.Shop.WheatBalance -= itemlist['Wheat']
			self.Shop.RiceBalance -= itemlist['Rice']
			self.Shop.SugarBalance -= itemlist['Sugar']
			self.Shop.KeroseneBalance -= itemlist['Kerosene']
			self.save()
			self.Shop.save()
			return (True,price)

		return (False,0)



def authenticateCustomer(rcno):
	try:
		cust = Customer.objects.get(RationCardNumber=rcno)
		return (cust!=None,cust)
	except:
		return (False,None)




class ComplaintLog(models.Model):
	RationId = models.ForeignKey(Customer,on_delete=models.CASCADE)
	Shop = models.ForeignKey(RationShop,on_delete=models.CASCADE)
	Complaint = models.TextField()




class ShopKeeper(models.Model):
	Fullname = models.CharField(max_length=20)
	Shop = models.ForeignKey(RationShop,on_delete=models.CASCADE)
	Hashed = models.BooleanField(default=False)
	Username = models.CharField(max_length=20,primary_key=True)
	Password = models.CharField(max_length=100)

	def save(self):
		if not self.Hashed:
			self.Password = str(hash(self.Password))
			self.Hashed = True

		super(ShopKeeper, self).save()

	def stockInfo(self):
		shop = self.Shop
		nAPL = shop.NumberOfAPLCostumers
		nBPL = shop.NumberOfBPLCostumers
		return {
			'Wheat' : shop.WheatBalance*100/(nAPL*wheat_apl_limit + nBPL*wheat_bpl_limit),
			'Rice' : shop.RiceBalance*100/(nAPL*rice_apl_limit + nBPL*rice_bpl_limit),
			'Sugar' : shop.SugarBalance*100/(nAPL*sugar_apl_limit + nBPL*sugar_bpl_limit),
			'Kerosene' : shop.KeroseneBalance*100/(nAPL*kerosene_apl_limit + nBPL*kerosene_bpl_limit),
		}

		


def authenticateShopKeeper(username,password):
        print hash(password)
        print username
        try:
	        s = ShopKeeper.objects.filter(Username=username,
			Password = str(hash(password))
			).first()
                print s
	        return (s!=None,s)
	except:
	        return (False,None)





