from django.conf.urls import url

from .views import check_status,depot_home

urlpatterns = [
    url('status',check_status),
    url('$',depot_home)
]
