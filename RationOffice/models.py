from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class RationOffice(models.Model):
	Location = models.CharField(max_length=50)
	NumberOfRationShops = models.SmallIntegerField()
	def __str__(self):
		return 'Location: {},No.of shops: {}'.format(self.Location,self.NumberOfRationShops)

class RationOfficer(models.Model):
	FullName = models.CharField(max_length=20)
	Office = models.ForeignKey(RationOffice,on_delete=models.CASCADE)
	Hashed = models.BooleanField(default=False)
	Username = models.CharField(max_length=20,primary_key=True)
	Password = models.CharField(max_length=100)

	def save(self):
		if not self.Hashed:
			self.Password = str(hash(self.Password))
			self.Hashed = True
		super(RationOfficer, self).save()

def authenticateRationOfficer(username,password):
	return RationOfficer.objects.filter(Username=username,
		Password = str(hash(password))
		).exists()



	







