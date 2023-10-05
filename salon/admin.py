from django.contrib import admin
from .models import Cart, CartItem, bookappointment, Products,seasonaloffers,alltimeoffers,otheroffers,discountoffers
# Register your models here.
admin.site.register(bookappointment)
admin.site.register(seasonaloffers)
admin.site.register(alltimeoffers)
admin.site.register(otheroffers)
admin.site.register(discountoffers)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(CartItem)
