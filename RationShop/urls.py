from django.conf.urls import url, include
import RationOffice.urls as OfficeUrls
from .views import *
urlpatterns = [
	    url(r'^login-customer',loginCustomer),
	    url(r'^verify',verify),
	    url(r'^all',allocateRation),
	    url(r'^buy',buy),
	    url(r'^balance',balance),
	    url(r'^login-shopkeeper',shopKeeperLogin),
	    url(r'^shopkeeper-data',shopKeeperData),
    ]