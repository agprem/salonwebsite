# from datetime import datetime
# from django.db import models
# from django .contrib.auth.models import User
# from PIL import Image
# import datetime

# # Create your models here.
# class UserProfile(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     email=models.EmailField(blank=True)
#     name=models.CharField(max_length=50,blank=False)
#     mobile=models.IntegerField(blank=False)
#     image=models.ImageField(default='default.jpg',upload_to='offer_pics')
#     address=models.TextField(blank=True)
#     dob=models.DateField(default=datetime.date.today())
    
#     def __str__(self):
#         return f'{self.user.name} Profile...'
        
    # def save(self,*args,**kwargs):                                   
    #     super().save(*args,**kwargs)                                   
    #     img=Image.open(self.image.path)
    #     if img.height>300 or img.width>300:               
    #         output_size=(300,300)                       
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,User
import datetime
from PIL import Image

from django.utils import timezone

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,mobile,password=None):
        if not mobile:
            raise ValueError("users must have mobile")
        user = self.model(mobile=mobile)
        print("Newusernormal created",user,mobile )
        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)
        print("Newuser saved  in user",user )
        return user

    def create_superuser(self,mobile,password):
        user = self.create_user(mobile,password=password)
        print("Newuser in superuser",user )
        user.set_password(password)
        user.is_admin= True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        print("Newuser saved in superuser",user,mobile )
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',blank=True)
    password=models.CharField(max_length=1000)
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=60,unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser =models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELD = []
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.name}'

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return self.is_admin


class UserProfile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='profile')
    address=models.TextField(blank=True)
    image=models.ImageField(default='default.jpg',upload_to='user_pics')
    dob = models.DateField(null=True,blank=True)

    def __str__(self):
        return f'{self.user} Profile '

           
    def save(self,*args,**kwargs):                                   
        super().save(*args,**kwargs)                                   
        img=Image.open(self.image.path)
        print("inimage of profile")
        if img.height>300 or img.width>300:               
            output_size=(200,200)                       
            img.thumbnail(output_size)
            img.save(self.image.path)