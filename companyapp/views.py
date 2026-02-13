from django.shortcuts import render
from django.http import HttpResponse
from . import views
from companyapp.models import tbl_service
from guestapp.models import tbl_company,tbl_login
from adminapp.models import tbl_category
from userapp.models import tbl_booking

# Create your views here.
def companyhome(request):
    return render(request,'Company/companyhome.html')

def service(request):
    cat=tbl_category.objects.all()
    return render(request,'Company/service.html', {'cat': cat})
def add_service(request):
    username=request.session.get('username')
    if username:
        if request.method == "POST":
            servname = request.POST.get("servicename")
            description= request.POST.get("desc")
            image=request.FILES.get('image')
            totalamount= request.POST.get("totalamount")
            categoryid = request.POST.get("categoryid")

            pob = tbl_service()
            pob.servicename = servname 

            pob.description = description
            pob.image = image 
            pob.totalamount =  totalamount 
            pob.categoryid = tbl_category.objects.get(categoryid=categoryid)
            pob.compid = tbl_company.objects.get(username=request.session['username'])
            if tbl_service.objects.filter(servicename=servname, compid=pob.compid).exists():
                return HttpResponse("<script>alert('Already Exists...');window.location='/companyapp/service';</script>")
            else:
            
                pob.save()
                return HttpResponse("<script>alert('Successfully inserted');window.location='/companyapp/service';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Login first');window.location='/guestapp/login';</script>")
    
def viewservices(request):
    loginid=request.session.get('loginid')
    if loginid:
        serv=tbl_service.objects.filter(compid=tbl_company.objects.get(loginid=request.session['loginid']))
        return render(request,'Company/viewservices.html',{'serv':serv})
    else:
        return HttpResponse("<script>alert('Authentication Required Login first');window.location='/guestapp/login';</script>")
def editservice(request,sid):
    if request.method =='POST':
        sob=tbl_service.objects.get(serviceid=sid)
        servname=request.POST.get("servicename")
        price=request.POST.get("totalamount")
        image=request.FILES.get("image")
        desc=request.POST.get("desc")
        categoryid=request.POST.get("categoryid")
        cat=tbl_category.objects.get(categoryid=categoryid)

        sob.servicename=servname
        sob.totalamount=price
        sob.image=image
        sob.description=desc
        sob.categoryid =cat
        sob.save()
        return viewservices(request)
    servob=tbl_service.objects.get(serviceid=sid)
    sob=servob
    catob=tbl_category.objects.all()
    cob=catob
    return render(request, 'Company/editservicepage.html',{'serv':sob,'categories':cob})
def deleteservice(request,sid):
    sob=tbl_service.objects.get(serviceid=sid)
    sob.delete()
    return viewservices(request)
def viewbookingrequests(request):
    loginid=request.session.get('loginid')
    if loginid:
        compid=tbl_company.objects.get(loginid=loginid)
        services=tbl_service.objects.filter(compid=compid)
        bookings=tbl_booking.objects.filter(serviceid__in=services)
        return render(request,'Company/viewbookingrequests.html',{'bookings':bookings})
    else:
        return HttpResponse("<script>alert('Authentication Required Login first');window.location='/guestapp/login';</script>")
def acceptbooking(request,bookingid):
    bob=tbl_booking.objects.get(bookingid=bookingid)
    bob.bookingstatus='Accepted'
    bob.save()
    return viewbookingrequests(request)
def rejectbooking(request,bookingid):
    bob=tbl_booking.objects.get(bookingid=bookingid)
    bob.bookingstatus='Rejected'
    bob.save()
    return viewbookingrequests(request)
def deletebooking(request,bookingid):
    bob=tbl_booking.objects.get(bookingid=bookingid)
    bob.delete()
    return viewbookingrequests(request)