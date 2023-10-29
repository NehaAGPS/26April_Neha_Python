from django.contrib import admin
from django.urls import path,include
from myapp import views


urlpatterns = [
    path('',views.getalldata),
    path('getstid/<int:id>',views.getstid),
    path('savestdata/',views.savestdata),
    path('deletestid/<int:id>',views.deletestid),
    path('updatedata/<int:id>',views.updatedata),
]