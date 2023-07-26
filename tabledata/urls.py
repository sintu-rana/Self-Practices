from django.urls import path
from tabledata.views import *

#urls-

urlpatterns = [
    path('dtl/', view_dtl),
    path('tabledata/', view_tabledata),
]
