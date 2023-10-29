from django.contrib import admin
from django.urls import path
from oppoapp import views

urlpatterns = [
   path('admin/',admin.site.urls),
   path('',views.index),
   path('oderadd/',views.oderadd),
   path('addproduct/',views.addproducts),
]