from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/<str:tipo>/', views.list, name='list'),
    path('add/<str:tipo>/', views.TipoTransaccionAdd, name='add'),
    path('edit/e/<int:id>/', views.updateE, name='updateE'),
    path('edit/i/<int:id>/', views.updateI, name='updateI'),
    path('edit/r/<int:id>/', views.updateR, name='updateR'),
    path('edit/ti/<int:id>/', views.updateTI, name='updateTI'),
	path('del/<int:id>/', views.TipoTransaccionDel, name='edit'),
    path('logout/', views.user_logout, name='user_logout'),
    path('create', views.create, name='create'),
    path('profile', views.profile, name='profile'),
    path('profile/edit/', views.profileedit, name='editprofile'),
    path('profile/edit/password', views.editPassword, name='editprofilePassword'),
]