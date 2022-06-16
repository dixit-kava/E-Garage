from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from garage.models import Garage,Service

def garageindex(request):
    return render(request,'gindex.html')

def handleGarageSignUp(request):
    if request.method=='POST':
        Gname=request.POST['garagename']
        Oname=request.POST['ownername']
        phone=request.POST['phoneno']
        address=request.POST['address']
        email=request.POST['email']
        password=request.POST['password']
        # print(name,email,phone,content)
        if len(Gname)<2 or len(email)<3 or len(phone)<10 or len(Oname)<2 or phone.isdigit()==False or len(address)<2:
            messages.error(request, "Please fill the form correctly")
        else:    
            ins = Garage(garagename=Gname,ownername=Oname,phone=phone,Address=address,email=email,password=password)
            ins.save()
            messages.success(request, "Your garage has been registered successfully")
            return redirect('/garage/')
    return render(request, 'Garagelogin.html')

def saveservices(request):
    return render(request,'adgs.html')

def myservices(request):
    if request.method=='POST':
        services1 = request.POST['services1']
        services2 = request.POST['services2']
        services3 = request.POST['services3']
        services4 = request.POST['services4']
        services5 = request.POST['services5']
        services6 = request.POST['services6']
        services7 = request.POST['services7']
        services8 = request.POST['services8']
        services9 = request.POST['services9']
        services10 = request.POST['services10']
        services11 = request.POST['services11']
        services12 = request.POST['services12']
        context = {'service1':services1,'service2':services2,'service3':services3,'service4':services4,'service5':services5,'service6':services6,'service7':services7,'service8':services8,'service9':services9,'service10':services10,'service11':services11,'service12':services12 }
        s = services1,services2,services3,services4,services5,services6,services7,services8,services9,services10,services11,services12
        ins = Service(services=s)
        ins.save()
        return render(request,'myservice.html',context)
    else:
        data = Service.objects.all()
        context={'data':data}
        return render(request,'myservice2.html',context)
        
        
    
        
    