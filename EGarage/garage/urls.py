from django.urls import path,include
from garage import views


urlpatterns = [
        path('Glogin/', views.handleGarageSignUp),
        path('addservices/', views.saveservices, name='saveservice'),
        path('addservices/myservices/', views.myservices, name='myservices'),
        path('addservices/myservices2/', views.myservices, name='myservices'),
        
]
