import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.api import error
from django.http import request
from django.http.response import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from .models import  Cart,CartItem, Products, bookappointment,seasonaloffers,alltimeoffers,otheroffers,discountoffers
from .forms import bookform
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied


app=0

# FOR SHOWING ALL OFFERS IN HOME.HTML    
def home(request):
    total=0
    context={}
    # FOR SHOWING NO OF ITEMS IN  CART------------------------------
    if request.user.is_authenticated:
        c=Cart.objects.filter(user=request.user,ordered=False)
        for i in c:
            c3=i.items.all()
            for j in c3:
                # print(total)
                total += j.quantity   # COUNT ITEMS IN CART WHICH IS NOT ORDERED YET AND THEN ADD THIS NO TO REQUEST.SESSION FOR SHOWING NO OF ITEMS IN CART ON HOMEPAGE
                # print(j.cartitem,j.quantity)
            print(total)
        request.session['cartitemnos']=total
    else:pass
    # FOR SHOWING OFFERS ON HOME PAGE-----------------
    seasonalofferobject=seasonaloffers.objects.first()
    alltimeofferobject=alltimeoffers.objects.first()
    otherofferobject=otheroffers.objects.first()
    discountofferobject=discountoffers.objects.first()
    productslist=Products.objects.all()

  
    context['seasonalofferobject']=seasonalofferobject
    context['alltimeofferobject']=alltimeofferobject
    context['otherofferobject']=otherofferobject
    context['discountofferobject']=discountofferobject
    context['productslist']=productslist
  
    

    return render(request,'salon/home.html',context)




	
# FOR BOOKING APPOINTMENT  IN APPOINTMENT AND HOME#BOOKAPPOINTMENT    
class bookappointments(LoginRequiredMixin,View):
    # print("hello IN BOOKAPPOINTMENTS")
    
    def get(self, request, *args, **kwargs):
        form = bookform()
        return render(request, 'salon/home.html')

    def post(self, request, *args, **kwargs):
        context={}
        global app
        print("inside post")
        form=bookform(request.POST)
        print("after form")
        data1=request.POST.get('service')
        data2=request.POST.get('time')
        data3=request.POST.get('date')
        print(form.errors,data1)
        
    
        if form.is_valid():
            print("inside valid")
            service=form.cleaned_data['service']
            date=form.cleaned_data['date']
            if date==datetime.date.today() and request.user.is_authenticated:
                print("hellodate",date,datetime.date.today(),app)
                if app>2:
                    messages.error(request,f'Booking full for this day')
                else:
                    app=app+1
                    print("insave",app)
                    form.instance.client=self.request.user
                    formvalue= form.save()
                    messages.success(request,f'Your Booking succesfull for {service} on {date}')



            else:
                print("serviceclean",form.cleaned_data['service'])
                form.instance.client=self.request.user
                formvalue= form.save()
                context['formvalue']=formvalue
                messages.success(request,f'Your Booking succesfull for {service} on {date}')
                return redirect("home")
        
        return redirect("book")



# FOR GETTING ALL SEASONAL OFFER BY ID IN SHOWOFFERS.HTML BOOK NOW BUTTON    
def get1_seasonaloffer(request,id):
    context={}
    offerdata=seasonaloffers.objects.get(id=id)
    print("seasonal",offerdata.offername)
    offerlist=seasonaloffers.objects.all()
    if offerdata.offerexp<datetime.date.today():
        context['offerlist']=offerlist
        messages.error(request,"Package is expired Please Choose other")
        return redirect("getall_seasonaloffer")
    else:context['service1']=offerdata.offername
    return render(request,'salon/appointment.html',context)



# FOR SHOWING ALL SEASONAL OFFERS IN SHOWOFFERS.HTML    
def getall_seasonaloffer(request):
    context={}
    print("hello in seasonaloffer")
    offerlist=seasonaloffers.objects.all()
    offerdata=seasonaloffers.objects.first()  # for getting name of offermodel in heading in template
    context['offerdata']=offerdata
    context['offerlist']=offerlist
    # print("offerlist",offerlist)
    context['today']=datetime.date.today()
    return render(request,'salon/showoffers.html',context)




#---ALLTIME OFFERS GETOFFER AND GETALL OFFER----------------------------------------------   >
def get1_alltimeoffer(request,id):
    context={}
    offerdata=alltimeoffers.objects.get(id=id)
    offerlist=alltimeoffers.objects.all()
    if offerdata.offerexp<datetime.date.today():
        context['offerlist']=offerlist
        messages.error(request,"This Package is expired Please Choose other")
        return redirect("getall_alltimeoffer")
    else:context['service1']=offerdata.offername
    return render(request,'salon/appointment.html',context)
    
            
def getall_alltimeoffer(request):
    print("hello in alloffer")
    context={}
    print("hello in alloffer")
    offerlist=alltimeoffers.objects.all()
    offerdata=alltimeoffers.objects.first()  # for getting name of offermodel in heading in template
    context['offerdata']=offerdata
    context['offerlist']=offerlist
    print("offerlist",offerlist)
    context['today']=datetime.date.today()
    return render(request,'salon/showoffers.html',context)
        



#---OTHER OFFERS GETOFFER AND GETALL OFFER----------------------------------------------   >   
def get1_otheroffer(request,id):
    context={}
    offerdata=otheroffers.objects.get(id=id)
    offerlist=otheroffers.objects.all()
    if offerdata.offerexp<datetime.date.today():
        context['offerlist']=offerlist
        messages.error(request,"Package is expired Please Choose other")
        return redirect("getall_otheroffer")
    else:context['service1']=offerdata.offername
    return render(request,'salon/appointment.html',context)


def getall_otheroffer(request):
    context={}
    print("hello in alloffer")
    offerlist=otheroffers.objects.all()
    offerdata=otheroffers.objects.first()  # for getting name of offermodel in heading in template
    context['offerdata']=offerdata
    context['offerlist']=offerlist
    # print("offerlist",offerlist)
    context['today']=datetime.date.today()
    return render(request,'salon/showoffers.html',context)


#---DISCOUNT OFFERS GETOFFER AND GETALL OFFER----------------------------------------------   >
def get1_discountoffer(request,id):
    context={}
    offerdata=discountoffers.objects.get(id=id)
    offerlist=discountoffers.objects.all()
    if offerdata.offerexp<datetime.date.today():
        context['offerlist']=offerlist
        messages.error(request,"Package is expired Please Choose other")
        return redirect("getall_discountoffer")
    else:context['service1']=offerdata.offername
    return render(request,'salon/appointment.html',context)
        
def getall_discountoffer(request):
    context={}
    print("hello in alloffer")
    offerlist=discountoffers.objects.all()
    offerdata=discountoffers.objects.first()  # for getting name of offermodel in heading in template
    context['offerdata']=offerdata
    context['offerlist']=offerlist
    # print("offerlist",offerlist)
    context['today']=datetime.date.today()
    return render(request,'salon/showoffers.html',context)

#---------------- OFFERS END---------------------------------------------------------------------

# # -----ADDING PRODUCTS TO CART ---------------------------------------------------------------------        
@login_required
def addtocart(request,id):
    total=0
    print("start total",total)
    product=get_object_or_404(Products,id=id)
    ordered_item,c=CartItem.objects.get_or_create(user=request.user,cartitem=product,ordered=False)
    order_qs=Cart.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        print("2")
        order=order_qs[0]
        print("order in add",(order.items))
        if order.items.filter (cartitem__id=id).exists():  # THIS CARTITEM__ID IS USED AS FOREIGN KEY IT MATCHED WITH PRODUCTID
            ordered_item.quantity = ordered_item.quantity + 1
            ordered_item.save()
            messages.success(request,f'Product added to cart Succesfully ')
        else:
            ordered_item.quantity = ordered_item.quantity + 1
            order.items.add(ordered_item)
            print("hello1")
            messages.success(request,f'Product added Succesfully')
    else:
        print("3")
        ordered_item.quantity = ordered_item.quantity + 1
        ordered_date=timezone.now()
        cart=Cart.objects.create(user=request.user,orderdate=ordered_date)
        cart.save()
        cart.items.add(ordered_item)
        messages.success(request,"Item added succesfully")

  
    return redirect("home")
    


# FOR SHOWING CART ON CLICKING CART IN HEADER-----------------------------------------

def  showcart(request):
    context={}
    total=0
    if request.user.is_authenticated:
        try:
             cart=Cart.objects.filter(user=request.user)
             #print(cart,"jhsdj")
             for i in cart:              # IT ITERATES THROUGH CARTOBJECTS AS ITEMS IS MANY TO MANY
                 cart1=i.items.all()
                 for j in cart1:
                     #print(j)
                     total= total+j.cartitem.price*j.quantity
             print("Total",total)
             context={'cartlist':cart1,'total':total}
             #print("out of cart")
             return render(request,'salon/cart.html',context)
        except:
            messages.error(request,"Cart is Empty")
            return render(request,"salon/cart.html")

    else:
        messages.error(request,"Login for Shopping Cart If not registered Please Register")
        return redirect("login")


def removecartitem(request,id):
    product=get_object_or_404(Products,id=id)
    ordered_item,c=CartItem.objects.get_or_create(user=request.user,cartitem=product,ordered=False)
    order_qs=Cart.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        print("2")
        order=order_qs[0]
        print("order in add",(order.items))
        if order.items.filter (cartitem__id=id).exists():
            if (ordered_item.quantity>1):
                ordered_item.quantity = ordered_item.quantity -1
                ordered_item.save()
                messages.success(request,f'Product Removed  Succesfully { ordered_item.quantity}')
            else:
                ordered_item=CartItem.objects.filter(cartitem=product,user=request.user,ordered=False)[0]
                order.items.remove(ordered_item)
                messages.success(request,f'Product Removed  Succesfully { ordered_item.quantity}')
        
        else:
            messages.info(request,"Item is not in your Cart") 
    else:return redirect("showcart")
    return redirect("showcart")

# FOR CLEARING COMPLETE CART--------------------   
def clearcart(request):
    items=Cart.objects.all()
    items.delete()
    messages.success(request,"Cart is empty now")
    return render(request,"salon/cart.html")




#---------REBOOK IN APPOINTMENT HISTORY------------------------------------------
        
def rebook(request,id):
    context={}
    bookingobject=bookappointment.objects.get(id=id)
    context['service1']=bookingobject.service
    print("service in rebook",bookingobject.service)
    return render(request,'salon/appointment.html',context)



# FOR CANCELLING APPOINTMENT IN APPOINTMENT HISTORY SECTION------------------------------------
def cancelapt(request,id):
    try:
        bookingobject=bookappointment.objects.get(id=id)
        print("indeleteapt",bookingobject)
        bookingobject.delete()
        messages.success(request,"Appointment Cancelled Succesfully")
    except ObjectDoesNotExist:
        messages.error(request,"Booking has been already Cancelled")
    return redirect("profile")