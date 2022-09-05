import email
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from crud.models import Employess


# view Employee
def home(request):
    emp = Employess.objects.all().order_by('-id')

    context = {
        'emp': emp
    }

    return render(request, "index.html", context)

# Add Employee


def add(request):
    if request.method == 'POST':
        nm = request.POST.get('name')
        em = request.POST.get('email')
        ad = request.POST.get('address')
        ph = request.POST.get('phone')

        empl = Employess(name=nm, email=em, address=ad, phone=ph)
        empl.save()
        return redirect('home')
    return render(request, "index.html")


# edit Employee
def edit(request):
    emp = Employess.objects.all()

    context = {
        'emp': emp
    }

    return redirect(request, "index.html", context)

# Update Employee


def update(request, id):
    if request.method == 'POST':
        nm = request.POST.get('name')
        em = request.POST.get('email')
        ad = request.POST.get('address')
        ph = request.POST.get('phone')

        empl = Employess(id=id, name=nm, email=em, address=ad, phone=ph)
        empl.save()
        return redirect('home')

    return redirect(request, "index.html")


# Delete Employee
def delete(request, id):
    emp = Employess.objects.filter(id=id).delete()

    context = {
        'emp': emp
    }
    return redirect('home')
