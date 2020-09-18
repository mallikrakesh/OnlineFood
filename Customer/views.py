from django.shortcuts import render
from Customer.middleware import LocaltionMiddleware
from Customer.middleware import returnAddress
from Vender.models import FoodItemsModel
from Myadmin.models import CityModel
from django.core.paginator import Paginator
import random
from Myadmin.otpsending import sendASMS
from Customer.models import CustomerRegistrationModel

# Create your views here.
def showIndex(request):
    res = returnAddress()
    data = FoodItemsModel.objects.all()
    p = Paginator(data,6)
    page_no = request.GET.get('pageno')
    if page_no:
        page = p.page(page_no)
    else:
        page = p.page(1)
    context = {"address": res[0], "city": res[1],'food':page}
    return render(request,'index.html',context)


def customer_register(request):
    return render(request,'customer/register.html',{'city':CityModel.objects.all()})


def customer_save(request):
    name = request.POST.get("c1")
    contact = request.POST.get("c2")
    address = request.POST.get("c3")
    city = request.POST.get("c4")
    password = request.POST.get("c5")
    otp = random.randint(100000 , 999999)
    message = "Hello Mr/Miss: " + name + ", Welcome to Online Food Order \n To complete Your Registration Use this OTP " + str(otp)
    sendASMS(contact , message)
    CustomerRegistrationModel(name=name,contact=contact,address=address,city_id=city,password=password,OTP=otp).save()
    return render(request,'customer/otp.html',{'contactNo':contact})


def customer_check_otp(request):
    try:
        CustomerRegistrationModel.objects.get(contact=request.POST.get("cno"), OTP=request.POST.get("otp"))
        return render(request, "customer/login.html",{"message": "Your Registration is Successful"})
    except CustomerRegistrationModel.DoesNotExist:
        return render(request, "customer/otp.html", {"contactNo": request.POST.get("cno"), "message": "Invalid OTP"})


def customer_login(request):
    return render(request,'customer/login.html')


def add_to_cart(request):
    return None


def customer_login_check(request):
    cn = request.POST.get("contact")
    pa = request.POST.get("password")
    print(cn,pa)
    return None