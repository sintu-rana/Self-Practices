from django.shortcuts import render, redirect
from tableforms.models import Student
from .forms import StudentForm

# Create your views here.

def view_dtl(request):
    resp=render(request, 'tableforms/dtl.html')
    return resp


def view_table(request):
    if request.method=='POST':
        resp=render(request, 'tableforms/table.html')
        return resp
    elif request.method=='GET':
        s=Student.objects.all()
        d1={'stu':s}
        resp=render(request, 'tableforms/tabledata.html', context=d1)
        return resp
    

def view_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tableforms/ registe/')  # Redirect to a success page
    else:
        form = StudentForm()

    return render(request, 'tableforms/register.html', {'form': form})
