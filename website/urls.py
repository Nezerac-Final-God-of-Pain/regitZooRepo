from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name=""),

    path('register', views.register, name='register'),

    path('my-login', views.my_login, name="my-login"),

    path('user-logout', views.user_logout, name="user-logout"),

    path('booking', views.booking, name="booking"),

    path('zoo-booking', views.make_zooBookings, name='zoo-booking')
]