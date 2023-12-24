from django.shortcuts import render,HttpResponse
from .models import Employee, Role, Departments
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
  return render(request,'index.html')


def all_emp(request):
  emps= Employee.objects.all()
  context= {
    'emps': emps
  }
  print(context)
  return render(request,'view_all_emp.html',context)

def add_emp(request):
  if request.method == 'POST':
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    salary = int(request.POST['salary'])
    bonus = int(request.POST['bonus'])
    phone = int(request.POST['phone'])
    role = int(request.POST['role'])
    dept = int(request.POST['dept'])
    hire_date = request.POST['hire_date']
    location= request.POST['location']
    new_emp=Employee(firstname=firstname,lastname=lastname,salary=salary,bonus=bonus,phone=phone,dept_id= dept,role_id=role,hire_date=datetime.now())
    new_emp.save()
    return HttpResponse('Employee added succesfully')
  elif request.method=='GET':
    return render(request,'add_emp.html')
  else :
    return HttpResponse('An Exception occured!,employee not added')
    


def remove_emp(request,emp_id=0):
  if emp_id:
    try:
      emp_to_be_removed=Employee.objects.get(id=emp_id)
      emp_to_be_removed.delete()
      return HttpResponse("Employee Removed Succesfully")
    except:
      return HttpResponse("Enter valid EMP ID")
    
  
  emps = Employee.objects.all()
  context = {
    'emps': emps
  }
  return render(request,'remove_emp.html',context)


def filter_emp(request):
  if request.method=='POST':
    name = request.POST['name']
    dept = request.POST['dept']
    role = request.POST['role']
    emps = Employee.objects.all()
    if name :
      emps = emps.filter(Q(firstname__icontains = name) | Q(lastname__icontains = name))
    if dept:
      emps = emps.filter(dept__name__icontains= dept)
    if role:
      emps = emps.filter(role__name__icontains= role)
    
    context= {
      'emps' : emps
    }
    return render(request,'view_all_emp.html',context)
  elif request.method == 'GET' :
    return render(request,'filter_emp.html')
  else:
    return HttpResponse("An exception occured")
   
  
