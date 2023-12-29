from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import UserDetails
# Create your views here.

def index(request):
    return render(request,'index_home.html')

def add(request):
    return render(request,'add.html')

def addrec(request):
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    organization=request.POST['organization']
    mobilenumber=request.POST['mobilenumber']
    mem=UserDetails(firstname=firstname,lastname=lastname,email=email,organization=organization,mobilenumber=mobilenumber)
    mem.save()
    return redirect("home")

def delete(request,id):
    mem=UserDetails.objects.get(id=id)
    mem.delete()
    return redirect("home")

def update(request,id):
    mem=UserDetails.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    organization=request.POST['organization']
    mobilenumber=request.POST['mobilenumber']
    profile_image=request.POST['profile_image']
    mem=UserDetails.objects.get(id=id)
    mem.firstname=firstname
    mem.lastname=lastname
    mem.email=email
    mem.organization=organization
    mem.mobilenumber=mobilenumber
    mem.profile_image=profile_image
    mem.save()
    return redirect('home')

@login_required(login_url='login')
def HomePage(request):
    user_status=request.user.is_staff

    if user_status==True:
        form_data=UserDetails.objects.all()
    else:
        email1=request.user.email
        form_data = UserDetails.objects.filter(email=email1) 

    context = {'form': form_data,'status':user_status}
    
    return render (request,'home.html',context)

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        mobilenumber=request.POST.get('mobilenumber')
        organization=request.POST.get('organization')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            my_details=UserDetails.objects.create(firstname=firstname,lastname=lastname,mobilenumber=mobilenumber,email=email,organization=organization)
            my_details.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')