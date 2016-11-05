from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import *
from depot.models import Approved
from RationShop.models import RationShop

def login(request):
	if request.method=='GET':
	    return render(request,'login.html',{})
	else:
		auth = authenticateRationOfficer(request.POST['username'],
		request.POST['password']
		)

		message = ["Unsuccessfull login","User successfully logged in"][auth]
	
		if auth:
			request.session['logged_in'] = True
		return render(request,'login.html',{'message':message})


def loggedin(request):
        return render(request,'ration_officer_home.html',{})

@csrf_exempt
def get_issues(request):
        try:
                R_O = RationOfficer.objects.get(Username=request.POST['username'])
        except:
                return JsonResponse({'status':False})
        print R_O
        complaints = ComplaintLog.objects.filter(Office=R_O.RationOffice)
        json_arr = []
        if complaints:
                json_arr = create_json(complaints)
        return JsonResponse({'status':True,'complaints':json_arr})

def create_json(complaints):
        mylist = list()
        for complaint in complaints:
                obj = dict()
                obj['name'] = complaint.RationId.Username
                obj['shopkeeper'] = complaint.Shop.ShopKeeper
                obj['location'] = complaint.Shop.Location
                obj['description']= complaint.Complaint
                mylist.append(obj)
        return mylist

def allocate(request):
        username = request.POST['username']
        officer = RationOfficer.objects.get(Username=username)
        ration_shops = RationShops.objects.filter(Office=officer.Office)
        print ration_shops
        for ration_shop in ration_shops:
                lis = Approved.objects.filter(RationShop = ration_shop)
                if(len(lis)!=0):
                        lis[0].Status=False
                        lis[0].save()
                else:
                        Approved.objects.create(RationShop=ration_shop)
        return JsonResponse({'status':True})

def approve(request):
        shop_id = request.GET['shop_id']
        approved = Approved.objects.filter(RationShop=shop_id)
        if(len(approved)!=0):
                approved[0].Status=True
                approved[0].save()
                return JsonResponse({'status':True})
        return JsonResponse({'status':False})
                
