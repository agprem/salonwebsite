from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import CustomUser, UserProfile



@receiver(post_save,sender=CustomUser)
def create_userprofile(sender,instance,created,**kwargs):
	print("in signals")
	if created:
		UserProfile.objects.create(user=instance)



@receiver(post_save,sender=CustomUser)  
def save_userprofile(sender,instance,**kwargs):  # we can name this function anything but profile is a attribute of User 
	print ("In signals save",instance)
	instance.profile.save()