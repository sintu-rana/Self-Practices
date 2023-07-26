from django.urls import path
from tableforms.views import *

#URLS-

urlpatterns = [
    path('dtl/',view_dtl),
    path('tabledata/',view_table, name='tabledata'),
    path('register/',view_register, name='register'),
]
