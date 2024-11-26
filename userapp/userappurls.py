from django.urls import path
from . import views
urlpatterns = [
    path('UserHome', views.userHome),
    path('ViewCategoryByUser', views.viewCategoryByUser),
    path('ViewFlavourByUser', views.viewFlavourByUser),
    path('ViewCakeByCategoryUser/<id>', views.viewCakeByCategoryUser, name='ViewCakeByCategoryUser'),
    path('ViewCakeByFlavourUser/<id>', views.viewCakeByFlavourUser, name='ViewCakeByFlavourUser'),
    path('ViewCakeDetailsByUser/<id>', views.viewCakeDetailsByUser, name='ViewCakeDetailsByUser'),
    path('CakeBooking/<id>', views.cakeBooking, name='CakeBooking'),
    path('ViewBookingByUser/<id>', views.viewBookingByUser),
    path('Payment/<id>', views.payment),
    path('ConfirmPayment/<id>', views.confirmPayment, name='ConfirmBooking'),
    path('ViewPaymentByUser/<id>', views.viewPaymentByUser),
    path('ViewCakeByUser', views.viewCakeByUser),
]