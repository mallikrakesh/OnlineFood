"""OnlineFood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from Vender import views

urlpatterns = [
    path('',views.showIndex,name='vendor_main'),
    path('vender_register/',views.venderRegister,name='vender_register'),
    path('vender_save/',views.venderSave,name='vender_save'),
    path('vendor_login_check/',views.vendor_login_check, name='vendor_login_check'),
    path('vendor_welcome/<int:pk>',views.vendor_welcome, name='vendor_welcome'),
    path('vendor_foodtype/',views.vendorFoodtype, name='vendor_foodtype'),
    path('vendor_save_foodtype/',views.vendor_save_foodtype, name='vendor_save_foodtype'),

    path('vendor_food/',views.vendorFood, name='vendor_food'),
    path('vendor_save_food/',views.vendor_save_food, name='vendor_save_food'),
]
