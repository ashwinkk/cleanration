from django.conf.urls import url

from .views import login,loggedin,get_issues,allocate,approve

urlpatterns=[
    url('login$', login),
    url('redir$', loggedin),
    url('issues$', get_issues),
    url('allocate$',allocate),
    url('approve',approve),
]    
