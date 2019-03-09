from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/<str:tipo_id>/', views.tipo_detail, name='detail'),
    path('edit/<str:tipo>/<str:id>/', views.TipoTransaccionEdit, name='edit'),
    path('logout/', views.user_logout, name='user_logout'),
]