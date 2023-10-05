from salon.models import bookappointment
from user.models import CustomUser
from django.shortcuts import render,redirect,HttpResponse
from .forms import LoginForm, UserRegisterForm,PasswordUpdateForm,ProfileUpdateForm,UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.utils import timezone
from django.views.generic import View


# Create your views here.


# --------- REGISTRATION ------------------------------------------------->

def register(request):
    print(request)
    uform=UserRegisterForm()
    if request.method =='POST':
        uform =UserRegisterForm(request.POST)
        # data1=request.POST.get('mobile')
        # print("MOBILEDATA",data1)
        print("REGFORM ERRORS",uform.errors)
        if uform.is_valid():    # VALIDATE WORKS ON CLEAN DATA
            print("INSIDE FORM VALIDATION")
            username=uform.cleaned_data.get('name')
            print("AFTER REGFORM VALIDATION" ,username,uform)
            user=uform.save()
            pw=user.password
            user.set_password(pw)
            user.save()
            messages.success(request,f' {username} Your account has been created ! Login Please')
            return redirect("login")
        else: 
            print("REGFORM IS NOT VALID")
            return render(request,"user/register.html",{'uform':uform})

           
        
    return render(request,"user/register.html",{'uform':uform})




# --------- USER-PROFILE------------------------------------------------->

@login_required
def profile(request):
    context={}
    print("HELLO INSIDE PROFILE FUNCTION")
    u_form=UserUpdateForm()
    p_form=ProfileUpdateForm()
    bookings=bookappointment.objects.filter(client=request.user)
    print("hello bookings",bookings)
    context={'u_form':u_form,'p_form':p_form,'bookings':bookings}
    if request.method=='POST':
        print("INSIDE PROFILE-UPDATE POST REQUEST")
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        print(u_form.errors, "and" ,p_form.errors)
        if  u_form.is_valid and p_form.is_valid():
            print("INSIDE PROFILEUPDATEFORM VALID")
            u_form.save()
            p_form.save()
            print(bookings)
            messages.success(request,f'Profile Updated Succesfully')
            return redirect("profile")
        else:
            print("INELSE OF PROFILEUPDATEFORM VALIDATION")
            u_form=UserUpdateForm(instance=request.user)
            p_form=ProfileUpdateForm(instance=request.user.profile)
            context={'p_form':p_form ,'u_form':u_form}
    return render(request,'user/profile.html',context)



# --------------------UPDATEPASSWORD-------------------------------------------------------------------------------------
class updatepassword(View):
    def get(self, request, *args, **kwargs):
        print("inside get of Paswordupdateform")
        form = PasswordUpdateForm(request.POST)
        return render(request, 'user/profile.html',{'form':form})
    def post(self, request, *args, **kwargs):
        print("inside Post of updateform")
        form=PasswordUpdateForm(request.POST)
        formerrors=form.non_field_errors
        
        if form.is_valid():
            oldpwd1=form.cleaned_data['oldpwd']
            newpwd=form.cleaned_data['newpwd']
            print("old",oldpwd1)
            user2=auth.authenticate(mobile=request.user.mobile,password=oldpwd1)
            # print("djhdhsj",user2,user2.password)
            try:
                if(user2==None):
                    messages.error(request,"Check Your Old Password")
                
                else:
                    request.user.set_password(newpwd)
                     # print(newpwd,request.user.set_password(newpwd))
                    request.user.save()
                    messages.success(request,"Your Password updated")
            except:return render(request,"user/profile.html",{'form':form})
            else:pass
        return render(request,'user/profile.html',{'form':form ,'formerrors':formerrors} )

        
            
        


# --------- LOGIN ------------------------------------------------>

def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    loginform=LoginForm()
    if request.method=="POST":
        # print("INSIDE LOGINFUNC POST")
        loginform=LoginForm(request.POST)
        # print("LOGINFORM ERRORS",loginform.errors)
        if loginform.is_valid():
            u_name=loginform.cleaned_data['username']
            p =loginform.cleaned_data['password']
            # print("u or p",u_name,p)
            try:
                if('@' in u_name):
                    user1=CustomUser.objects.get(email=u_name)
                    usermobile=user1.mobile
                    print("INSIDE @ usermobile",usermobile)
                    user_check =auth.authenticate(mobile=usermobile, password=p)
                    print("inside @",user_check)
                else:
                    user_check =auth.authenticate(mobile=u_name, password=p)
                    # print("INSIDE MOBILE AUTHENTICATION")
                if user_check is not None:
                    # print("INSIDE USERCHECK")
                    user_check.last_login= timezone.now()
                    user_check.save(update_fields=['last_login'])
                    auth.login(request, user_check)
                    print("USER-LOGGED-IN AS",user_check)
                    messages.success(request,"You have been Logged in ")
                    return redirect ("home")
                else:
                    messages.error(request,f'Unauthorised User')
                    return redirect("login")

            except:messages.error(request,"Username or Password not Correct")   

        else:return redirect("login")
    
    return render(request,'user/login.html',{'form':loginform}) 


# --------- LOGOUT ------------------------------------------------->

def logout(request):
    auth.logout(request)
    return redirect("home")

