from django.urls import path
from tablecrud.views import *

#URLS-

urlpatterns = [
    path('dtl/', view_dtl, name='dtl'),
    path('register/', view_register, name='register'),
    path('data/', view_data, name='data'),
    path('delete/<id>/', view_delete, name='delete'),
    path('update/<id>/', view_update, name='update'),
    
]
