from django.urls import path
from . import views

urlpatterns = [
    path('', views.guestHome),
    path('Login', views.login,name='Login'),
    path('Logout', views.logout, name='Logout'),
    path('ViewCategory', views.viewCategory),
    path('ViewFlavour', views.viewFlavour),
    path('ViewCakeByCategory/<id>', views.viewCakeByCategory, name='ViewCakeByCategory'),
    path('ViewCakeByFlavour/<id>', views.viewCakeByFlavour, name='ViewCakeByFlavour'),
    path('ViewCakeDetails/<id>', views.viewCakeDetails, name='ViewCakeDetails'),
    path('GuestRegistration', views.guestRegistration, name='GuestRegistration'),
    path('ViewCakeByGuest', views.viewCakeByGuest),
]