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

from Customer import views

urlpatterns = [
    path('',views.showIndex,name='customer_home'),
    path('customer_register',views.customer_register,name='customer_register'),
    path('customer_save',views.customer_save,name='customer_save'),
    path('customer_check_otp',views.customer_check_otp,name='customer_check_otp'),
    path('customer_login',views.customer_login,name='customer_login'),
    path('customer_login_check',views.customer_login_check,name='customer_login_check'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
]
