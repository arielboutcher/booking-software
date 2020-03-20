from django.urls import path
from alabooking import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('customer/<str:pk>/', views.customer, name = 'customer'),

    path('register/', views.register, name = 'register'),
    path('login/', views.loginPage, name = 'login'),
    path('logout', views.logoutUser, name = "logout"),
    path('profile/<int:pk>/', views.profile, name = 'profile'),

    path('booking/', views.createBooking, name= "booking"),
]
