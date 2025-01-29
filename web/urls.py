from django.urls import path
from . import views

urlpatterns = [    
path('login/', views.loginPage, name= 'login'),
path('user_list/', views.user_list, name= 'user_list'),
path('insert/', views.insert, name= 'insert'),
path('logout/', views.logoutUser, name= 'logout'),
path('register/', views.registerPage, name= 'register'),
path('', views.home, name='home'),
path('index/<str:pk>/', views.index, name='index'),
path('createRoom/', views.createRoom, name='createRoom'),
path('updateRoom/<str:pk>/', views.updateRoom, name='updateRoom'),
path('deleteRoom/<str:pk>/', views.deleteRoom, name='deleteRoom'),
]