from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/<str:tipo>/', views.list, name='list'),
    path('miscortes/', views.listCorte, name='listCorte'),
    path('cortes/<int:id>/', views.listCorteDet, name='listCorteDet'),
    path('cortes/genera/', views.GeneraCorte, name='GeneraCorte'),
    path('edit/e/<int:id>/', views.updateE, name='updateE'),
    path('edit/i/<int:id>/', views.updateI, name='updateI'),
    path('edit/r/<int:id>/', views.updateR, name='updateR'),
    path('edit/p/<int:id>/', views.updateP, name='updateTI'),
    path('add/e/', views.createE, name='createE'),
    path('add/i/', views.createI, name='createI'),
    path('add/r/', views.createR, name='createR'),
    path('add/p/', views.createP, name='createP'),
	path('delete/<str:tipo>/<int:id>/', views.delete, name='delete'),
    path('logout/', views.user_logout, name='user_logout'),
    path('create', views.create, name='create'),
    path('profile', views.profile, name='profile'),
    path('profile/edit/', views.profileedit, name='editprofile'),
    path('profile/add/user', views.adduser, name='crearusuario'),
    path('profile/edit/password', views.editPassword, name='editprofilePassword'),
]