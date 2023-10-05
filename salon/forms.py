

from django import forms

from. models import bookappointment

class bookform(forms.ModelForm):
    print("inside forms.")
    time=forms.TimeField(required=False)
    class Meta:
        model=bookappointment
        fields=['service','technician','date','time']
        
       

