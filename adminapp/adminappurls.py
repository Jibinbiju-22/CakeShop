from django.urls import path
from . import views

urlpatterns = [
    path('AdminHome', views.adminHome),
    path('CategoryRegistration', views.categoryRegistration, name='CategoryRegistration'),
    path('FlavourRegistration', views.flavourRegistration, name='FlavourRegistration'),
    path('CakeRegistration', views.cakeRegistration, name='CakeRegistration'),
    path('ViewBookingByAdmin', views.viewBookingbyAdmin),
    path('ConfirmBooking/<id>', views.confirmBooking),
    path('AcceptBooking/<id>', views.acceptbooking),
    path('DeleteBooking/<id>', views.deletebooking),
    path('ViewPayment', views.viewPayment),
    path('ViewApproval', views.viewApproval),
    path('ConfirmAsDelivered/<id>', views.confirmAsDelivered),
    path('ViewPurchase', views.viewPurchase),
    path('ViewCategoryByAdmin', views.viewCategoryByAdmin),
    path('ViewFlavourByAdmin', views.viewFlavourByAdmin),
    path('ViewCakeByAdmin', views.viewCakeByAdmin)
]