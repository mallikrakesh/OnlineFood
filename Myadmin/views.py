from django.shortcuts import render,redirect
from django.contrib import messages
from Myadmin.models import *
from Vender.models import VendorRegistrationModel
from Myadmin.otpsending import sendASMS

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
        return render(request, "myadmin/login.html", {"error": "Admin Logout Successfully"})


def myadmin_welcome(request):
    return render(request,'myadmin/welcome.html')

# State Operation

def openState(request):
    return render(request,"myadmin/openstate.html",{"state_data": StateModel.objects.all()})

def saveState(request):
    if request.POST.get("upd_idno"):
        sm = StateModel.objects.get(id=request.POST.get("upd_idno"))
        sm.name = request.POST.get("state")
        if not request.FILES.get("photo"):
            pass
        else:
            sm.photo = request.FILES.get("photo")
        sm.save()
        messages.success(request,'Updated Successfully')
        return render(request, "myadmin/openstate.html",{ "state_data": StateModel.objects.all()})
    else:
        try:
            StateModel(name=request.POST.get("state"), photo=request.FILES.get("photo")).save()
            messages.success(request, "State Added Successfully")
            return redirect('state')

        except:
            StateModel.objects.get(name=request.POST.get("state"))
            messages.error(request,'State Already Exist')
            return render(request, "myadmin/openstate.html",{ "state_data": StateModel.objects.all()})


def updateState(request):
    idno = request.GET.get("idno")
    sm = StateModel.objects.get(id=idno)
    context={"idno": sm.id, "state": sm.name, "photo": sm.photo, "state_data": StateModel.objects.all()}
    return render(request, "myadmin/openstate.html",context)

def deleteState(request):
    print(request.GET.get("idno"))
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
        messages.success(request,'Updated Successfully')
        return render(request, "myadmin/opencity.html",{"city_data": CityModel.objects.all(),"state": StateModel.objects.only('name')})
    else:
        try:
            CityModel(name=request.POST.get("city"), photo=request.FILES.get("photo"), city_state_id=request.POST.get("state")).save()
            messages.success(request, "City Added Successfully")
            return redirect('city')
        except:
            CityModel.objects.get(name=request.POST.get("city"))
            messages.error(request, "City Already Exist")
            return render(request, "myadmin/opencity.html",{"city_data": CityModel.objects.all()})


def updateCity(request):
    cm = CityModel.objects.get(id= request.GET.get("idno"))
    context = {"idno": cm.id, "city_state":cm.city_state.id, "city": cm.name, "photo": cm.photo, "city_data": CityModel.objects.all(),"state":StateModel.objects.only('name')}
    return render(request, "myadmin/opencity.html",context)


def deleteCity(request):
    CityModel.objects.get(id=request.GET.get("idno")).delete()
    return redirect('city')

#Cusine Operation

def openCusine(request):
    return render(request,"myadmin/opencuisine.html")

def saveCuisine(request):
    if request.POST.get("upd_idno"):
        cm=CuisineModel.objects.get(id=request.POST.get("upd_idno"))
        cm.type=request.POST.get("cuisine")
        if not request.FILES.get("photo"):
            pass
        else:
            cm.photo=request.FILES.get("photo")
        cm.save()
        messages.success(request,"Updated Successfully")
        return render(request,"myadmin/opencuisine.html",{"cuisine_data": CuisineModel.objects.all()})
    else:
        try:
            CuisineModel.objects.get(type=request.POST.get("cuisine"))
            messages.error(request,"Cuisine Already Exist")
            return render(request, "myadmin/opencuisine.html", {"cuisine_data": CuisineModel.objects.all()})
        except:
            CuisineModel(type=request.POST.get("cuisine"), photo=request.FILES.get("photo")).save()
            messages.success(request, "Cuisine Added")
            return redirect('cuisine')


def updateCuisine(request):
    idno=request.GET.get("idno")
    cm=CuisineModel.objects.get(id=idno)
    context = {"idno":cm.id,"cuisine":cm.type,"photo":cm.photo,"cuisine_data":CuisineModel.objects.all()}
    return render(request,"myadmin/opencuisine.html",context)

def deleteCuisine(request):

    CuisineModel.objects.get(id=request.GET.get("idno")).delete()
    return redirect('cuisine')



def openVendor(request):
    return render(request,"myadmin/openvendor.html",{"pending":VendorRegistrationModel.objects.filter(status="pending"),"approved":VendorRegistrationModel.objects.filter(status="approved")})

def admin_vendor_approve(request):
    res = VendorRegistrationModel.objects.get(id=request.GET.get("idno"))
    sname = res.stall_name
    cno = res.contact_1
    res.status = 'approved'
    res.save()
    sendASMS(str(cno), "Hello " + sname + "! \n We are happy to inform that your registration is approved by Admin")
    return openVendor(request)

def openReporsts(request):
    return render(request,"myadmin/openreports.html")