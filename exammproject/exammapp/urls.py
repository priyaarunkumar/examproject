from django.contrib import admin
from django.urls import path,include
from . import views
app_name='exammapp'
urlpatterns = [

    path('',views.fun,name='fun'),
    path('login/',views.login,name='login'),
    path('register/', views.register, name='register'),
    path('movie/<int:id>/', views.details,name='details'),
    path('log/',views.log,name='log'),
    path('deliver/',views.deliver,name='deliver'),
    path('regi/',views.regi,name='regi'),
    path('add/', views.person_create_view, name='add'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('order/', views.order, name='order'),
    path('ajax/load-prize/', views.load_prize, name='ajax_load_prize'),
    path('success/', views.success, name='success'),
]
