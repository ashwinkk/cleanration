from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt

import json
# Create your views here.

from .models import *
from sendOtp import sendOTP
from random import randint

import json


def verifiedCustomer(request):
	return Customer.objects.get(RationCardNumber=request.body['card_no']).Verified


@csrf_exempt
def loginCustomer(request):
	print request.body
	data = json.loads(request.body)
	customer = Customer.objects.get(RationCardNumber=data['card_no'])
	otp = randint(100000,999999)
	sendOTP(otp,customer.PhoneNumber)
	customer.LastSentOTP = otp
	customer.save()
	return JsonResponse({
		'success' : True
		})



@csrf_exempt
def verify(request):
	print request.body
	data = json.loads(request.body)
	otp = int(data['otp'])
	customer = Customer.objects.get(RationCardNumber=data['card_no'])
	if customer.LastSentOTP == otp:
		customer.Verified = True
		customer.LastSentOTP = None
	else:
		customer.Verified = False	
	customer.save()
	return JsonResponse({
			'success': True,
			'verified' : customer.Verified,
			'card_type' : customer.CardType,
			'shop_no' : customer.Shop_id, 
			})



@csrf_exempt
def buy(request):
        print request.body

	data = json.loads(request.body)
	data = json.loads(data['json'])
	data_to = {
		'Wheat' : float(data['Wheat']),
		'Rice' : float(data['Rice']),
		'Sugar' : float(data['Sugar']),
		'Kerosene' : float(data['Kerosene'])
	}

        print data['card_no']
	try:
		cust = Customer.objects.get(RationCardNumber=data['card_no'])
	except:
		print 'Invalid card_no'
		return JsonResponse({
				'success' : False,
				})

	if cust.Verified:
		success,price = cust.purchase(data_to)
		return JsonResponse({
				'success' : success,
				'price' : price,
				})

	else:
		return JsonResponse({
				'success' : False,
				})




def allocateRation(request):
	
	for e in Customer.objects.all():
		e.allocate()

	for e in RationShop.objects.all():
		e.allocate()

	return JsonResponse({'message' : 'success'})




@csrf_exempt
def balance(request):
        print request.body
	data = json.loads(request.body)
	
	try:
		cust = Customer.objects.get(RationCardNumber=data['card_no'])
	except:
		print 'Invalid card_no'
		return JsonResponse({
				'success' : False,
				})

	if cust.Verified:
		balance_data = cust.balance()
                
		return JsonResponse({
				'success' : True,
				'balance' : balance_data,
				})

	else:
		return JsonResponse({
				'success' : False,
				})



@csrf_exempt
def shopKeeperLogin(request):
	#data = request.POST
	data = json.loads(request.body)
	print data
	auth,shopkeeper = authenticateShopKeeper(str(data['username']),str(data['password']))
	
	return JsonResponse({
			'success' : True,
		})


@csrf_exempt
def shopKeeperData(request):
	#data = request.POST
	data = json.loads(request.body)
        print data['password']
	auth,shopkeeper = authenticateShopKeeper(str(data['username']),str(data['password']))
	if auth:
		return JsonResponse({
				'success' : True,
				'chart-data' : shopkeeper.stockInfo(), 
			})
	else:
		return JsonResponse({
				'success' : False,
			})


