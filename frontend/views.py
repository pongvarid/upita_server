from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from requests import auth

login_valid = 'admin.2022'
pwd_valid = 'admin.2022.up'

def close(req):
    return render(req,'close.html')

def index(req):
    return render(req,'index.html')

def authenticatePlan(request):
    user = authenticate(request, username=login_valid, password=pwd_valid)
    if user is not None:
        login(request, user)
        year = request.GET.get('year')
        agency = request.GET.get('agency')
        return redirect('/super-up-plan-admin/moral_organization/baseplan/add/?_popup=1&agency='+agency+'&year='+year)

def editPlan(request):
    user = authenticate(request, username=login_valid, password=pwd_valid)
    if user is not None:
        login(request, user)
        id = request.GET.get('id')
        return redirect('/super-up-plan-admin/moral_organization/baseplan/'+id+'/change/?_popup=1')


def adminSignExercise(request):
    user = authenticate(request, username=login_valid, password=pwd_valid)
    if user is not None:
        login(request, user)
        id = request.GET.get('id')
        return redirect('/super-up-plan-admin/moral_organization/signadminexercise/add/?_popup=1&id='+id)

def passingSignExercise(request):
    user = authenticate(request, username=login_valid, password=pwd_valid)
    if user is not None:
        login(request, user)
        id = request.GET.get('id')
        return redirect('/super-up-plan-admin/moral_organization/signpassingexercise/add/?_popup=1&id='+id)
