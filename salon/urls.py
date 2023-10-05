
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('book/',views.bookappointments.as_view(),name="book"),
    path('getall_seasonaloffer/',views.getall_seasonaloffer,name="getall_seasonaloffer"),
    path('getall_seasonaloffer/<int:id>',views.get1_seasonaloffer,name="get1_seasonaloffer"),
    
    path('getall_alltimeoffer/',views.getall_alltimeoffer,name="getall_alltimeoffer"),
    path('getall_alltimeoffer/<int:id>',views.get1_alltimeoffer,name="get1_alltimeoffer"),
    
    path('getall_otheroffer/',views.getall_otheroffer,name="getall_otheroffer"),
    path('getall_otheroffer/<int:id>',views.get1_otheroffer,name="get1_otheroffer"),
    
    path('getall_discountoffer/',views.getall_discountoffer,name="getall_discountoffer"),
    path('getall_discountoffer/<int:id>',views.get1_discountoffer,name="get1_discountoffer"),

    path('rebook/<int:id>',views.rebook,name="rebook"),
    path('cancelapt/<int:id>',views.cancelapt,name="cancelapt"),
   
    path('addtocart/<int:id>',views.addtocart,name="addtocart"),
    path('showcart/',views.showcart,name="showcart"),
    path("removecartitem/<int:id>/",views.removecartitem,name="removecartitem"),
    path('clearcart/',views.clearcart,name='clearcart'),






]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)