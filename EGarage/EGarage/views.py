
from django.shortcuts import render,redirect
from django.http import HttpResponse
from customer.models import contact
from garage.models import Garage,Service
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout



def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def privacy(request):
    return render(request,'privacy.html')

def terms(request):
    return render(request,'terms.html')

def FaQ(request):
    return render(request,'faqs.html')

def signup(request):
    return render(request,'Signup.html')

def security(request):
    return render(request,'security.html')
def map(request):
    return render(request,'mapp.html')

def history(request):
    return render(request,'history.html')

def bservices(request):
    return render(request,'bservice.html')

def settings(request):
    return render(request,'settings.html')

def demo(request):
    garagedata = Garage.objects.all()
    servicedata = Service.objects.all()
    mylist=zip(garagedata,servicedata) 
    context = {'mylist':mylist}
    return render(request,'demoo.html', context)



def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
    
        if not name.isalnum() or len(name)==0:
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('Sup')
        if len(pass1)<3:
             messages.error(request, " Passwords do not match")
             return redirect('Sup')
            
        if (pass1!= pass2):
            messages.error(request, " password length is very small...")
            return redirect('Sup')
        if len(email)<3:
             messages.error(request, " incorrect email")
             return redirect('Sup')
        if len(phone)<10:
             messages.error(request, " incorrect phone number")
             return redirect('Sup')
        # Create the user
        myuser = User.objects.create_user(name, email, pass1) 
        myuser.phone= phone
        myuser.pass2= pass2
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('home')
    else:
        return HttpResponse("404 - Not found")
    
    

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginname']
        loginpassword=request.POST['loginpass']
        user=authenticate(username= loginusername, password= loginpassword) 
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    else:
        return HttpResponse("404- Not found")
    
    
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

def contactus(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        # print(name,email,phone,content)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4 or phone.isdigit()==False:
            messages.error(request, "Please fill the form correctly")
        else:    
            c = contact(username=name,userphone=phone,useremail=email,usercontent=content)
            c.save()
            messages.success(request, "Your message has been successfully sent")
            return redirect('home')
       
    return render(request,'contactus.html')


def userprofile(request):
    return render(request,'userprofile.html')

def smot(request):
    return render(request,'smot.html')

def servicing(request):
    return render(request,'servicing.html')

def repairs(request):
    return render(request,'repairs.html')

def selectservice(request):
    return render(request,'selectservices.html')
