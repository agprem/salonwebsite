from django import forms
from django.contrib.auth import authenticate
from django.db.models.fields import DateTimeField
from django.http.response import HttpResponse
from .models import CustomUser,UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
import re


# --------- USER REGISTERATION FORM------------------------------------->

class UserRegisterForm(forms.ModelForm):
    print("inside regform of user")
    email=forms.EmailField(label="email",help_text="email should have special character")
    class Meta:
        model=CustomUser
        fields=['name','password','mobile','email']
    def clean(self):
        regex="[^a-zA-Z0-9]"
        specialch=re.compile(regex)
        pass1=self.cleaned_data['password']
        print("i am pass1",pass1)
        if(re.search(specialch,pass1)):
            print("inside regex")
            if(len(pass1)<=5 ):
                print(len(pass1))
                password=pass1
                print ("password in validation",password,pass1)
                raise ValidationError("Password length should be greater then 5 characters")
        else:raise ValidationError("Password should contain a special Character")


# --------- LOGIN FORM------------------------------------------------->

class LoginForm(forms.Form):
    password = forms.CharField(label='password',widget=forms.PasswordInput)
    username=forms.CharField(max_length='1000')
    
       
# --------- USER PROFILE FORM------------------------------------------------->

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['dob','address','image']



class UserUpdateForm(forms.ModelForm):    # we are merging two forms for user detail and image field in Profile Model
   class Meta:
        model=CustomUser
        fields=['name','mobile','email']
   



# --------- PASSWORD UPDATE FORM------------------------------------------------->

class PasswordUpdateForm(forms.Form):
    oldpwd=forms.CharField(required=True)
    newpwd=forms.CharField(required=True)
    cfmpwd=forms.CharField(required=True)
    
    def clean(self):
        oldpwd=forms.CharField(required=True)
        newpwd=self.cleaned_data['newpwd']
        regex="[^a-zA-Z0-9]"
        specialch=re.compile(regex)
        pass1=self.cleaned_data['newpwd']
        print("i am pass1",pass1)
        if(re.search(specialch,pass1)):
            print("inside regex")
            if(len(pass1)<=5 ):
                print(len(pass1))
                password=pass1
                print ("password in validation",newpwd,pass1)
                raise ValidationError("NewPassword length should be greater then 5 characters")
        else:raise ValidationError("NewPassword should contain a special Character")


        cfmpwd=self.cleaned_data['cfmpwd']
        print("inclean ",newpwd ,cfmpwd)
        if(newpwd!=cfmpwd):
            print("inside Error")
            raise forms.ValidationError("Your Password field and Confirm Password Field do not Match")
        
    
        
