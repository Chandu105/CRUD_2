from django.shortcuts import render
from app.models import *
from django.db.models import Q

# Create your views here.
def display_dept(request):
    QLDO=Dept.objects.all()
    QLDO=Dept.objects.filter(Q(deptno=10) | Q(loc='NEWYORK'))
    QLDO=Dept.objects.all()
    d={'Dept':QLDO}
    return render(request,'display_dept.html',d)

def display_emp(request):
    QLEO=Emp.objects.all()
    d={'QLEO':QLEO}
    return render(request,'display_emp.html',d)


def insert_dept(request):
    dn=input('enter dept no: ')
    n=input('enter dname: ')
    l=input('enter loc : ')
    DNO=Dept.objects.get_or_create(deptno=dn,dname=n,loc=l)[0]
    DNO.save()
    QLDO=Dept.objects.all()
    d={'Dept':QLDO}
    return render(request,'display_dept.html',d)

def insert_emp(request):
    en=input('empno : ')
    ena=input('empname:')
    j=input('job:')
    m=input('mgr:')
    h=input('hiredate:')
    s=input('sal:')
    c=input('comm:')
    d=input('deptno:')

    DO=Dept.objects.get(dname=ena)

    EMO=Emp.objects.get_or_create(ename=DO,empno=en,job=j,mgr=m,hiredate=h,sal=s,comm=c,deptno=d)[0]
    EMO.save()
    QLEO=Emp.objects.all()
    d={'QLEO':QLEO}
    return render(request,'display_emp.html',d)

    
    