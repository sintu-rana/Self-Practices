from django.urls import path
from .views import *

#urls-

urlpatterns = [
    path('', view_base),
    path('register/', view_register, name="register"),
    path('login/', view_login, name="login"),
    path('logout/', view_logout, name="logout_page"),
]
