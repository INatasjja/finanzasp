from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/<str:tipo>/', views.list, name='list'),
    path('add/<str:tipo>/', views.TipoTransaccionAdd, name='add'),
    path('edit/<str:tipo>/<int:id>/', views.update, name='edit'),
	path('del/<int:id>/', views.TipoTransaccionDel, name='edit'),
    path('logout/', views.user_logout, name='user_logout'),
    path('create', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('profile', views.profile, name='profile'),
    path('profile/edit/', views.profileedit, name='editprofile'),
    path('profile/edit/password', views.editPassword, name='editprofilePassword'),
]