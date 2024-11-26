from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, Case, When, Value, IntegerField

from adminapp.models import *
from userapp.models import *

# Create your views here.


def userHome(request):
    loginid = request.session.get('loginid')
    category = tblcategory.objects.all()
    flavour = tblflavour.objects.all()
    user = tbluser.objects.get(loginid=loginid)
    return render(request, 'User/UserHome.html', {'loginid': loginid, 'category': category, 'flavour': flavour, 'user': user})


def viewCategoryByUser(request):
    category = tblcategory.objects.all()
    return render(request, 'User/ViewCategoryByUser.html', {'category': category})


def viewFlavourByUser(request):
    flavour = tblflavour.objects.all()
    return render(request, 'User/ViewFlavourByUser.html', {'flavour': flavour})


def viewCakeByCategoryUser(request, id):
    category = tblcategory.objects.get(categoryid=id)
    cake = tblcake.objects.filter(categoryid=id)
    return render(request, 'User/ViewCakeByCategoryUser.html', {'cake': cake, 'category': category})


def viewCakeByFlavourUser(request, id):
    flavour = tblflavour.objects.get(flavourid=id)
    cake = tblcake.objects.filter(flavourid=id)
    return render(request, 'User/ViewCakeByFlavourUser.html', {'cake': cake, 'flavour': flavour})


def viewCakeDetailsByUser(request, id):
    cake = tblcake.objects.get(cakeid=id)
    return render(request, 'User/ViewCakeDetailsByUser.html', {'cake': cake})


def cakeBooking(request, id):
    if request.method == 'POST':
        deliveryaddress = request.POST.get('deliveryaddress')
        requireddate = request.POST.get('requireddate')
        quantity = request.POST.get('quantity')
        totalamount = request.POST.get('totalamount')
        bookingstatus = 'Requested'
        cakeid = tblcake.objects.get(cakeid=id)
        loginid = request.session.get('loginid')


        bookingobj = tblbooking()
        bookingobj.deliveryaddress = deliveryaddress
        bookingobj.requireddate = requireddate
        bookingobj.quantity = quantity
        bookingobj.totalamount = totalamount
        bookingobj.bookingstatus = bookingstatus
        bookingobj.cakeid = cakeid
        bookingobj.loginid = tbllogin.objects.get(loginid=loginid)
        bookingobj.save()

        return HttpResponse(
            f"<script>alert('Booking request successfully submitted');"
            f"window.location='/User/ViewBookingByUser/{loginid}';</script>"
        )
    else:
        cake = tblcake.objects.get(cakeid=id)
        return render(request, 'User/CakeBooking.html', {'cake': cake})


def viewBookingByUser(request, id):
    booking = tblbooking.objects.filter(
        Q(bookingstatus='Requested') | Q(bookingstatus='Confirmed'),
        loginid=id
    )
    return render(request, 'User/ViewBookingByUser.html', {'booking': booking})


def payment(request, id):
    booking = tblbooking.objects.get(bookingid=id)
    return render(request, 'User/Payment.html', {'booking': booking})


def confirmPayment(request, id):
    if request.method == 'POST':
        booking = tblbooking.objects.get(bookingid=id)
        if booking.bookingstatus == 'Confirmed':
            booking.bookingstatus = 'Paid'
            booking.save()
            return HttpResponse("<script>alert('Payment successful.');window.location='/User/UserHome';</script>")
        else:
            return HttpResponse(
                "<script>alert('Something went wrong try again later.');window.location='/User/UserHome';</script>")
    else:
        booking = tblbooking.objects.get(bookingid=id)
        return render(request, 'User/ConfirmPayment.html', {'booking': booking})


def viewPaymentByUser(request, id):
    booking = tblbooking.objects.filter(
        Q(bookingstatus='Paid') | Q(bookingstatus='Delivered'),
        loginid=id
    ).annotate(
        status_order=Case(
            When(bookingstatus='Paid', then=Value(0)),
            When(bookingstatus='Delivered', then=Value(1)),
            output_field=IntegerField(),
        )
    ).order_by('status_order')

    return render(request, 'User/ViewPaymentByUser.html', {'booking': booking})

def viewCakeByUser(request):
    cake = tblcake.objects.all()
    return render(request, 'User/ViewCakeByUser.html', {'cake': cake})
