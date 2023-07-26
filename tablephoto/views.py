from django.shortcuts import render
from tablephoto.models import Employee

# Create your views here.

def view_dtl(request):
    resp=render(request, 'tablephoto/dtl.html')
    return resp

def view_tablephoto(request):
    if request.method=='POST':
        resp=render(request, 'tablephoto/tablephoto.html')
        return resp
    elif request.method=='GET':
        s=Employee.objects.all()
        d1={'emp':s}
        resp=render(request, 'tablephoto/tablephoto.html', context=d1)
        return resp