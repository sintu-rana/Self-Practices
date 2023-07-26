from django.shortcuts import render, redirect
from tablecrud.models import Customer

# Create your views here.

def view_dtl(request):
    resp=render(request, 'tablecrud/dtl.html')
    return resp

def view_register(request):

    if request.method=='POST':

        data=request.POST
        
        name=data.get('name')
        age=data.get('age')
        address=data.get('address')
        mobile=data.get('mobile')
        pic=request.FILES.get('pic')


        Customer.objects.create(
            name=name,
            age=age,
            address=address,
            mobile=mobile,
            pic=pic
        )

    return render(request, 'tablecrud/register.html')

def view_data(request):
    if request.method=='POST':
        resp=render(request, 'tablecrud/data.html')
        return resp
    elif request.method=='GET':
        s=Customer.objects.all()
        d1={'cus':s}
        resp=render(request, 'tablecrud/data.html',context=d1)
        return resp
    
def view_delete(request, id):
    queryset=Customer.objects.get(id = id)
    queryset.delete()
    return redirect('/tablecrud/data/')

def view_update(request, id):
    queryset=Customer.objects.get(id = id)

    if request.method=="POST":
        data=request.POST

        name=data.get('name')
        age=data.get('age')
        address=data.get('address')
        mobile=data.get('mobile')
        pic=request.FILES.get('pic')

        queryset.name=name
        queryset.age=age
        queryset.address=address
        queryset.mobile=mobile

        if pic:
            queryset.pic=pic

        queryset.save()
        return redirect('/tablecrud/data/')
        

    context={'cus':queryset}
    return render(request,'tablecrud/update.html', context)
    
    