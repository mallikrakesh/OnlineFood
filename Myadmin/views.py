from django.shortcuts import render,redirect
from django.contrib import messages
from Myadmin.models import *

# Create your views here.
def showIndex(request):
    return render(request,'myadmin/login.html')

def myadmin_login_check(request):
    if request.method == "POST":
        try:
            admin = AdminLoginModel.objects.get(username=request.POST.get("username"),password=request.POST.get("password"))
            request.session["admin_status"] = True
            return redirect('welcome')
        except:
            return render(request, "myadmin/login.html", {"error": "Invalid User"})
    else:
        request.session["admin_status"] = False
        return render(request, "myadmin/login.html", {"error": "Admin Logout Success"})


def myadmin_welcome(request):
    return render(request,'myadmin/welcome.html')

def openState(request):
    return render(request,"myadmin/openstate.html",{"state_data": StateModel.objects.all()})

# State Operation
def saveState(request):
    if request.POST.get("upd_idno"):
        sm = StateModel.objects.get(id=request.POST.get("upd_idno"))
        sm.name = request.POST.get("state")
        if not request.FILES.get("photo"):
            pass
        else:
            sm.photo = request.FILES.get("photo")
        sm.save()
        return render(request, "myadmin/openstate.html",{"success": "Updated Successfully", "state_data": StateModel.objects.all()})
    else:
        try:
            StateModel(name=request.POST.get("state"), photo=request.FILES.get("photo")).save()
            messages.success(request, "State Added")
            return redirect('state')

        except:
            StateModel.objects.get(name=request.POST.get("state"))
            return render(request, "myadmin/openstate.html",{"error": "State Already Exist", "state_data": StateModel.objects.all()})


def updateState(request):
    idno = request.GET.get("idno")
    sm = StateModel.objects.get(id=idno)
    return render(request, "myadmin/openstate.html",{"idno": sm.id, "state": sm.name, "photo": sm.photo, "state_data": StateModel.objects.all()})

def deleteState(request):
    print(request.GET.get("idno"))
    print(type(request.GET.get("idno")))
    StateModel.objects.get(id=request.GET.get("idno")).delete()
    return redirect('state')


def openCity(request):
    return render(request,"myadmin/opencity.html",{"state":StateModel.objects.all(),"city_data":CityModel.objects.all()})
def saveCity(request):
    if request.POST.get("upd_idno"):
        cm = CityModel.objects.get(id=request.POST.get("upd_idno"))
        cm.name = request.POST.get("city")
        if not request.FILES.get("photo"):
            pass
        else:
            cm.photo = request.FILES.get("photo")
        print(cm.city_state)
        print(cm.city_state.id)
        print(request.POST.get("city_state"))
        print(request.POST.get("state"))
        sm = StateModel.objects.get(id=request.POST.get("state"))
        cm.city_state.id = sm
        cm.save()
        return render(request, "myadmin/opencity.html",{"success": "Updated Successfully", "city_data": CityModel.objects.all(),"state": StateModel.objects.only('name')})
    else:
        try:
            CityModel(name=request.POST.get("city"), photo=request.FILES.get("photo"), city_state_id=request.POST.get("state")).save()
            messages.success(request, "City Added")
            return redirect('city')
        except:
            CityModel.objects.get(name=request.POST.get("city"))
            return render(request, "myadmin/opencity.html",{"error": "City Already Exist", "city_data": CityModel.objects.all()})


def updateCity(request):
    cm = CityModel.objects.get(id= request.GET.get("idno"))
    return render(request, "myadmin/opencity.html",{"idno": cm.id, "city_state":cm.city_state.id, "city": cm.name, "photo": cm.photo, "city_data": CityModel.objects.all(),"state":StateModel.objects.only('name')})


def deleteCity(request):
    CityModel.objects.get(id=request.GET.get("idno")).delete()
    return redirect('city')

def openCusine(request):
    return render(request,"myadmin/opencuisine.html")
#Cusine Operation
def saveCuisine(request):
    if request.POST.get("upd_idno"):
        cm=CuisineModel.objects.get(id=request.POST.get("upd_idno"))
        cm.type=request.POST.get("cuisine")
        if not request.FILES.get("photo"):
            pass
        else:
            cm.photo=request.FILES.get("photo")
        cm.save()
        return render(request,"myadmin/opencuisine.html",{"success":"Updated Successfully","cuisine_data": CuisineModel.objects.all()})
    else:
        try:
            CuisineModel.objects.get(type=request.POST.get("cuisine"))
            return render(request, "myadmin/opencuisine.html",
                          {"error": "Cuisine Already Exist", "cuisine_data": CuisineModel.objects.all()})
        except:
            CuisineModel(type=request.POST.get("cuisine"), photo=request.FILES.get("photo")).save()
            messages.success(request, "Cuisine Added")
            return redirect('cuisine')


def updateCuisine(request):
    idno=request.GET.get("idno")
    cm=CuisineModel.objects.get(id=idno)
    return render(request,"myadmin/opencuisine.html",{"idno":cm.id,"cuisine":cm.type,"photo":cm.photo,"cuisine_data":CuisineModel.objects.all()})

def deleteCuisine(request):
    print(request.GET.get("idno"))
    print(type(request.GET.get("idno")))
    CuisineModel.objects.get(id=request.GET.get("idno")).delete()
    return redirect('cuisine')



def openVendor(request):
    return render(request,"myadmin/openvendor.html")


def openReporsts(request):
    return render(request,"myadmin/openreports.html")


