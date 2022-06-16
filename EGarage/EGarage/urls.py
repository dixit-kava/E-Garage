
from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path,include
from . import views
from garage import views as gv
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about),
    path('FaQ/', views.FaQ),
    path('signup/', views.signup, name='Sup'),
    path('handleSignup', views.handleSignUp),
    path('privacy', views.privacy),
    path('terms', views.terms),
    path('security', views.security),
    path('handleSignup', views.handleSignUp),
    path('demo', views.demo),
    path('map', views.map),
    path('garage/', include('garage.urls')),
    path('userprofile', views.userprofile),
    path('history', views.history),
    path('bservices', views.bservices),
    path('settings', views.settings),
    path('contactus/', views.contactus),
    path('garage/', gv.garageindex), 
    path('login', views.handeLogin, name='login'),
    path('logout', views.handelLogout, name="handleLogout"),
    path('garage/Glogin/logout', views.handelLogout, name="handleLogout"),
    path('accounts/', include('allauth.urls')),
    path("accounts/profile/", TemplateView.as_view(template_name="Signup.html")),
    path('smot/', views.smot, name='smot'),
    path('servicing/', views.servicing, name='servicing'),
    path('repairs/', views.repairs, name='repairs'),
    path('selectservices', views.selectservice),
    path('customer/',include('customer.urls')) 
    

]
