from django.shortcuts import render
from django.http import HttpResponse
from guestapp.models import *
from adminapp.models import *
from userapp.models import *
from django.shortcuts import redirect

# Create your views here.


def guestHome(request):
    category = tblcategory.objects.all()
    flavour = tblflavour.objects.all()
    return render(request, 'Guest/GuestHome.html', {'category': category, 'flavour': flavour})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if tbllogin.objects.filter(username=username, password=password).exists():
            loginobj = tbllogin.objects.get(username=username, password=password)
            request.session['loginid'] = loginobj.loginid
            loginid = request.session['loginid']
            role = loginobj.role
            if role == 'admin':
                return HttpResponse("<script>window.location='/Admin/AdminHome';</script>")
            elif role == 'user':
                return HttpResponse("<script>window.location='/User/UserHome';</script>")
        else:
            return HttpResponse(
                "<script>alert('Invalid username or password');window.location='/Guest/Login';</script>")
    else:
        return render(request, 'Guest/Login.html')


def logout(request):
    if "loginid" in request.session:
        del request.session["loginid"]
        return redirect('/Guest/Login')


def viewCategory(request):
    category = tblcategory.objects.all()
    return render(request, 'Guest/ViewCategory.html', {'category': category})


def viewFlavour(request):
    flavour = tblflavour.objects.all()
    return render(request, 'Guest/ViewFlavour.html', {'flavour': flavour})


def viewCakeByCategory(request, id):
    category = tblcategory.objects.get(categoryid=id)
    cake = tblcake.objects.filter(categoryid=id)
    return render(request, 'Guest/ViewCakeByCategory.html', {'cake': cake, 'category': category})


def viewCakeByFlavour(request, id):
    flavour = tblflavour.objects.get(flavourid=id)
    cake = tblcake.objects.filter(flavourid=id)
    return render(request, 'Guest/ViewCakeByFlavour.html', {'cake': cake, 'flavour': flavour})


def viewCakeDetails(request, id):
    cake = tblcake.objects.get(cakeid=id)
    return render(request, 'Guest/ViewCakeDetails.html', {'cake': cake})


def guestRegistration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        contactnumber = request.POST.get('contactnumber')
        password = request.POST.get('password')
        profilephoto = request.FILES['profilephoto']
        if tbllogin.objects.filter(username=username).exists():
            return HttpResponse(
                "<script>alert('Username already exist');window.location='/Guest/GuestRegistration';</script>")
        if tbluser.objects.filter(contactnumber=contactnumber).exists():
            return HttpResponse(
                "<script>alert('Contact number already exist');window.location='/Guest/GuestRegistration';</script>")
        loginobj = tbllogin()
        loginobj.username = username
        loginobj.password = password
        loginobj.role = 'user'
        userobj = tbluser()
        userobj.name = name
        userobj.username = username
        userobj.contactnumber = contactnumber
        userobj.password = password
        userobj.profilephoto = profilephoto
        loginobj.save()
        userobj.loginid = loginobj
        userobj.save()
        return HttpResponse("<script>alert('Registration successful');window.location='/Guest/Login';</script>")
    else:
        return render(request, 'Guest/GuestRegistration.html')


def viewCakeByGuest(request):
    cake = tblcake.objects.all()
    return render(request, 'Guest/ViewCakeByGuest.html', {'cake': cake})
