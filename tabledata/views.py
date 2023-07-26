from django.shortcuts import render
from tabledata.models import Student

# Create your views here.

def view_dtl(request):
    resp=render(request, 'tabledata/dtl.html')
    return resp

def view_tabledata(request):
    if request.method=='POST':
        resp=render(request, 'tabledata/tabledata.html')
        return resp
    elif request.method=='GET':
        s=Student.objects.all()
        d1={'stu':s}
        resp=render(request, 'tabledata/tabledata.html', context=d1)
        return resp