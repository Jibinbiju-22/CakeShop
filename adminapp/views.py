from django.shortcuts import render
from django.http import HttpResponse

from userapp.models import *
from adminapp.models import *

from django.db.models import Q, Case, When, Value, IntegerField


# Create your views here.

def adminHome(request):
    user = tbluser.objects.all()
    pay = tblbooking.objects.filter(
        Q(bookingstatus='Paid') | Q(bookingstatus='Delivered')
    ).annotate(
        status_order=Case(
            When(bookingstatus='Paid', then=Value(0)),
            When(bookingstatus='Delivered', then=Value(1)),
            output_field=IntegerField(),
        )
    ).order_by('status_order')
    return render(request, 'Admin/AdminHome.html', {'user': user, 'pay': pay})

def categoryRegistration(request):
    if request.method == 'POST':
        categoryname = request.POST.get('categoryname')
        categoryphoto = request.FILES['categoryphoto']
        categoryobj = tblcategory()
        if tblcategory.objects.filter(categoryname=categoryname).exists():
            return HttpResponse(
                "<script>alert('Category already exist');window.location='/Admin/CategoryRegistration';</script>")
        else:
            categoryobj.categoryname=categoryname
            categoryobj.categoryphoto=categoryphoto
            categoryobj.save()
            return HttpResponse(
                "<script>alert('Category registration successful');window.location='/Admin/ViewCategoryByAdmin';</script>"
            )
    else:
        return render(request, 'Admin/CategoryRegistration.html')

def flavourRegistration(request):
    if request.method == 'POST':
        flavourname = request.POST.get('flavourname')
        flavourobj = tblflavour()
        if tblflavour.objects.filter(flavourname=flavourname).exists():
            return HttpResponse(
                "<script>alert('Flavour already exist');window.location='/Admin/FlavourRegistration';</script>")
        else:
            flavourobj.flavourname=flavourname
            flavourobj.save()
            return HttpResponse(
                "<script>alert('Flavour registration successful');window.location='/Admin/ViewFlavourByAdmin';</script>"
            )
    else:
        return render(request, 'Admin/FlavourRegistration.html')

def cakeRegistration(request):
    if request.method == 'POST':
        cakename = request.POST.get('cakename')
        cakedescription = request.POST.get('cakedescription')
        cakeweight = request.POST.get('cakeweight')
        amount = request.POST.get('amount')
        cakephoto = request.FILES['cakephoto']
        categoryid = tblcategory.objects.get(categoryid=request.POST.get('categoryid'))
        flavourid = tblflavour.objects.get(flavourid=request.POST.get('flavourid'))
        if tblcake.objects.filter(cakename=cakename).exists():
            return HttpResponse(
                "<script>alert('Cake already exist');window.location='/Admin/CakeRegistration';</script>")
        else:
            cakeobj = tblcake()
            cakeobj.cakename = cakename
            cakeobj.cakedescription = cakedescription
            cakeobj.cakeweight = cakeweight
            cakeobj.amount = amount
            cakeobj.cakephoto = cakephoto
            cakeobj.categoryid = categoryid
            cakeobj.flavourid = flavourid
            cakeobj.save()
            return HttpResponse(
                "<script>alert('Cake registration successful');window.location='/Admin/ViewCakeByAdmin';</script>")
    else:
        category = tblcategory.objects.all()
        flavour = tblflavour.objects.all()
        return render(request, 'Admin/CakeRegistration.html', {'category': category, 'flavour': flavour})


def viewBookingbyAdmin(request):
    booking = tblbooking.objects.filter(bookingstatus='Requested')
    return render(request, 'Admin/ViewBookingByAdmin.html', {'booking': booking})

def confirmBooking(request, id):
    # Fetch the booking instance using the bookingid
    booking = tblbooking.objects.get(bookingid=id)

    # Fetch the login instance associated with the booking (through the loginid ForeignKey)
    login = booking.loginid  # This gives you the related tbllogin instance

    # Fetch the user instance associated with the login instance (through the loginid ForeignKey in tbluser)
    user = tbluser.objects.get(loginid=login)  # This gives you the related tbluser instance

    return render(request, 'Admin/ConfirmBooking.html', {'booking': booking, 'user': user})


def deletebooking(request, id):
    booking = tblbooking.objects.get(
        bookingid=id)  # To delete a record in a table, start by getting the record you want to delete:
    if booking.bookingstatus == 'Requested':
        booking.delete()  # call delete() function to perform delete operation
        return HttpResponse(
            "<script>alert('The order has been successfully rejected.');window.location='/Admin/ViewBookingByAdmin';</script>")
    else:
        return HttpResponse(
            "<script>alert('Something wrong. Try again!');window.location='/Admin/ViewBookingByAdmin';</script>")


def acceptbooking(request, id):
    booking = tblbooking.objects.get(bookingid=id)
    if booking.bookingstatus == 'Requested':
        booking.bookingstatus = 'Confirmed'
        booking.save()
        return HttpResponse("<script>alert('Booking accepted.');window.location='/Admin/ViewApproval';</script>")
    else:
        return HttpResponse(
            "<script>alert('Something wrong. Try again later.');window.location='/Admin/AdminHome';</script>")


def viewPayment(request):
    # Filter bookings where booking status is 'Paid'
    bookings = tblbooking.objects.filter(bookingstatus='Paid')

    # Prepare a list of users corresponding to the paid bookings
    users = [tbluser.objects.get(loginid=booking.loginid) for booking in bookings]

    # Zip the bookings and users lists together
    bookings_with_users = zip(bookings, users)

    return render(request, 'Admin/ViewPayment.html', {'bookings_with_users': bookings_with_users})



def viewApproval(request):
    booking = tblbooking.objects.filter(bookingstatus='Confirmed')
    return render(request, 'Admin/ViewApproval.html', {'booking': booking})


def confirmAsDelivered(request, id):
    booking = tblbooking.objects.get(bookingid=id)
    if booking.bookingstatus == 'Paid':
        booking.bookingstatus = 'Delivered'
        booking.save()
        return HttpResponse(
            "<script>alert('The status has been successfully changed.');window.location='/Admin/ViewPurchase';</script>")
    else:
        return HttpResponse(
            "<script>alert('Something wrong. Try again later');window.location='/Admin/AdminHome';</script>")



def viewPurchase(request):
    # Filter bookings where booking status is 'Delivered'
    bookings = tblbooking.objects.filter(bookingstatus='Delivered')

    # Prepare a list of users corresponding to the delivered bookings
    users = [tbluser.objects.get(loginid=booking.loginid) for booking in bookings]

    # Zip the bookings and users lists together
    bookings_with_users = zip(bookings, users)

    return render(request, 'Admin/ViewPurchase.html', {'bookings_with_users': bookings_with_users})


def viewCategoryByAdmin(request):
    category = tblcategory.objects.all()
    return render(request, 'Admin/ViewCategoryByAdmin.html', {'category': category})


def viewFlavourByAdmin(request):
    flavour = tblflavour.objects.all()
    return render(request, 'Admin/ViewFlavourByAdmin.html', {'flavour': flavour})


def viewCakeByAdmin(request):
    cake = tblcake.objects.all()
    return render(request, 'Admin/ViewCakeByAdmin.html', {'cake': cake})


