from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from .models import Approved
from RationShop.models import RationShop 

# Create your views here.

def depot_home(request):
    return render(request,'depot.html',{})

@csrf_exempt
def check_status(request):
    ration_id = request.GET.get('ration_id')
    try:
        app_object = Approved.objects.get(RationShop=ration_id)
    except:
        return JsonResponse({'status': False})
    if(app_object.Status == True):
        return JsonResponse({'status':True,'text':'Already Approved'})
    return JsonResponse({'status':True,'text':'Pending'})
