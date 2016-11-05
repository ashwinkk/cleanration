# select choice and enter data in space separated form

''' 
open django shell and:
from RationOffice.populate_db import func
func()
'''

from RationOffice.models import RationOffice,RationShop

def func():
	print '1.RationOffice\n2.RationShop'

	ch = int(raw_input())

	args = raw_input().split()

	if ch==1:
		RationOffice.objects.create(
			Location = args[0],
			NumberOfRationShops = int(args[1]),
			)
	else:
		r = RationShop.objects.create(
			Location = args[0],
			NumberOfCustomers = int(args[1]),
			RationOffice_id	= RationShop.objects.first().id,
			)


