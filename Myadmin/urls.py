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

from Myadmin import views

urlpatterns = [
    path('',views.showIndex,name='admin_home'),
    path('myadmin_login_check/',views.myadmin_login_check,name='myadmin_login_check'),
    path('welcome/',views.myadmin_welcome,name='welcome'),

    #State Operation
    path('state/', views.openState, name='state'),
    path('saveState/',views.saveState,name='saveState'),
    path('updateState/',views.updateState,name="updateState"),
    path('deleteState/',views.deleteState,name="deleteState"),

    # City Operation
    path('city/', views.openCity, name='city'),
    path('saveCity/', views.saveCity, name='saveCity'),
    path('updateCity/', views.updateCity, name="updateCity"),
    path('deleteCity/', views.deleteCity, name="deleteCity"),

    # Cusine Operation
    path('cuisine/', views.openCusine, name='cuisine'),
    path('saveCuisine/', views.saveCuisine, name="saveCuisine"),
    path('updateCuisine/', views.updateCuisine, name="updateCuisine"),
    path('deleteCuisine/', views.deleteCuisine, name="deleteCuisine"),

    path('vendor/', views.openVendor, name='vendor'),
    path('resports/', views.openReporsts, name='reports'),







]
