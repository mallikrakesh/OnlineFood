from django.contrib import messages
from django.shortcuts import render,redirect
from Myadmin.models import CuisineModel, CityModel
from Vender.models import VendorRegistrationModel,FoodTypeModel,FoodItemsModel


def showIndex(request):
    return render(request, 'vendor/login.html')

def venderRegister(request):
    return render(request, "vendor/register.html",{"cuisine": CuisineModel.objects.all(), "city": CityModel.objects.all()})


def venderSave(request):
    sn = request.POST.get("v1")
    c1 = request.POST.get("v2")
    c2 = request.POST.get("v3")
    cui = request.POST.get("v4")
    ph = request.FILES.get("v5")
    add = request.POST.get("v6")
    cty = request.POST.get("v7")
    pas = request.POST.get("v8")
    otp = 0000
    sta = "pending"
    VendorRegistrationModel(stall_name=sn, contact_1=c1, contact_2=c2, cuisine_type_id=cui, photo=ph, address=add,vendor_city_id=cty, password=pas, OTP=otp, status=sta).save()
    messages.success(request, "Registration is Done, Need To Approval from Admin")
    return redirect('vendor_main')

def vendor_login_check(request):
    if request.method == "POST":
        try:
            vender_data = VendorRegistrationModel.objects.get(contact_1=request.POST.get('username'),password=request.POST.get('password'),status='approved')
            request.session["vendor_status"] = True
            return redirect('vendor_welcome',pk=vender_data.id)
        except:
            return render(request, "vendor/login.html", {"error": "Invalid User"})
    else:
        request.session["vendor_status"] = False
        return render(request, "vendor/login.html", {"error": "Vendor Logout Success"})


def vendor_welcome(request,pk):
    request.session["vendor_id"] = pk
    vendor_details = VendorRegistrationModel.objects.get(id=pk)
    return render(request,'vendor/vendor_welcome.html',{"vendor_data":vendor_details})


def vendorFoodtype(request):
    vendor_details = VendorRegistrationModel.objects.get(id=request.session['vendor_id'])
    context= {"vendor_data": vendor_details,"food_type": FoodTypeModel.objects.filter(vendor_id_id=request.session['vendor_id'])}
    print(context)
    return render(request, "vendor/foodtype.html",context)


def vendor_save_foodtype(request):
    FoodTypeModel(name=request.POST.get("f1"), vendor_id_id=request.session['vendor_id'],status=request.POST.get("f2")).save()
    return vendorFoodtype(request)


def vendorFood(request):
    vendor_details = VendorRegistrationModel.objects.get(id=request.session["vendor_id"])
    context = {"vendor_data": vendor_details, "food_type": FoodTypeModel.objects.filter(vendor_id_id=request.session["vendor_id"]),"food": FoodItemsModel.objects.filter(food_type__vendor_id=request.session["vendor_id"])}
    return render(request, "vendor/food.html",context)


def vendor_save_food(request):
    FoodItemsModel(name=request.POST.get("f1"), food_type_id=request.POST.get("f2"), price=request.POST.get("f3"),photo=request.FILES.get('f4')).save()
    return vendorFood(request)