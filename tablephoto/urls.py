from django.urls import path
from tablephoto.views import *

#URLs-

urlpatterns = [
    path('dtl/', view_dtl),
    path('tablephoto/', view_tablephoto),

]
