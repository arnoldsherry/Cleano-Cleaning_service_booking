from django.shortcuts import render
from django.http import HttpResponse
from adminapp.models import tbl_category
from companyapp.models import tbl_service
from guestapp.models import tbl_login,user
from userapp.models import tbl_booking
from django.http import JsonResponse
from userapp.models import tbl_payment
from datetime import datetime
from django.db.models import Count  
# Create your views here.
def index(request):
    return render(request,'User/index.html')
def searchservice(request):
    category=tbl_category.objects.all()
    return render(request,'User/searchservice.html',{'cat':category})
def fillservices(request):
    categoryid = int(request.POST.get("cid"))
    services = tbl_service.objects.filter(categoryid=categoryid).values()
    return JsonResponse(list(services),safe=False) 
def servicepage(request,serviceid):
    serviceid = serviceid
    service = tbl_service.objects.get(serviceid=serviceid)
    return render(request,'User/servicepage.html',{'services':[service]})
def bookservice(request):
    loginid=request.session.get('loginid')
    if loginid:
        if request.method=='POST':
            bookingdate=request.POST.get('bookingdate')
            bookingstatus=request.POST.get('bookingstatus')
            serviceid=request.POST.get('serviceid')
            try:
                booking_date_obj = datetime.strptime(bookingdate, '%Y-%m-%d').date()
                if booking_date_obj < datetime.now().date():
                    return HttpResponse("<script>alert('Booking date cannot be in the past. Please select a valid date.');window.location='/userapp/servicepage/{{ serviceid }}';</script>")
            except ValueError:
                return HttpResponse("<script>alert('Invalid date format');window.location='/userapp/servicepage/{{serviceid}}';</script>")
            
            uob=user.objects.get(loginid=loginid)
            userid=uob.userid
            bob=tbl_booking()
            bob.bookingdate=bookingdate
            bob.bookingstatus=bookingstatus
            bob.serviceid=tbl_service.objects.get(serviceid=serviceid)
            bob.userid=user.objects.get(userid=userid)
            if tbl_booking.objects.filter(bookingdate=bob.bookingdate, userid=bob.userid, bookingstatus="Accepted").exists():
                return HttpResponse("<script>alert('Already Exists...');window.location='/userapp/mybookings';</script>")
            else:
            
                bob.save()
                return HttpResponse("<script>alert('Booked Successfully.Company will verify your request');window.location='/userapp/mybookings';</script>")
        else:
            return HttpResponse("<script>alert('Authentication Required! Login first');window.location='/guestapp/login';</script>")
def mybookings(request):
    loginid=request.session.get('loginid')
    if loginid:
        uob=user.objects.get(loginid=loginid)
        past_bookings = tbl_booking.objects.filter(userid=uob, bookingdate__lt=datetime.now().date())
        past_bookings.delete()
        bookings = tbl_booking.objects.filter(userid=uob)
        return render(request,'User/mybookings.html',{'bookings':bookings})
    else:
        return HttpResponse("<script>alert('Authentication Required Login first');window.location='/guestapp/login';</script>")
def paymentpage(request,bookingid):
    loginid=request.session.get('loginid')
    if loginid:
        uob=user.objects.get(loginid=loginid)
        booking=tbl_booking.objects.get(bookingid=bookingid, userid=uob)
        return render(request,'User/paymentpage.html',{'booking':booking})
def cancelbooking(request,bookingid):
    loginid=request.session.get('loginid')
    if loginid:
        uob=user.objects.get(loginid=loginid)
        booking=tbl_booking.objects.get(bookingid=bookingid, userid=uob)
        booking.delete()
        return HttpResponse("<script>alert('Booking Cancelled Successfully');window.location='/userapp/mybookings';</script>")
def deletebooking(request,bookingid):
    loginid=request.session.get('loginid')
    if loginid:
        uob=user.objects.get(loginid=loginid)
        booking=tbl_booking.objects.get(bookingid=bookingid, userid=uob)
        booking.delete()
        return HttpResponse("<script>alert('Booking Deleted Successfully');window.location='/userapp/mybookings';</script>")
def pay(request):
    loginid=request.session.get('loginid')
    if loginid:
        if request.method=='POST':
            bookingid=request.POST.get("bookingid")
            totalamount=request.POST.get("totalamount")
            bookingdate=request.POST.get("bookingdate")
            paymentstatus=request.POST.get("paymentstatus")
            paymentdate=request.POST.get("paymentdate")
            uob=user.objects.get(loginid=loginid)
            userid=uob.userid
            pob=tbl_payment()
            pob.bookingid=tbl_booking.objects.get(bookingid=bookingid)
            pob.totalamount=totalamount
            pob.paymentstatus=paymentstatus
            pob.paymentdate=paymentdate
            bob=tbl_booking.objects.get(bookingid=bookingid)
            bob.bookingstatus='Paid'
            bob.save()
            pob.save()
            return HttpResponse("<script>alert('Payment Successful');window.location='/userapp/mybookings';</script>")
        else:
            return HttpResponse("<script>alert('Invalid Request Method');window.location='/userapp/mybookings';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Login first');window.location='/guestapp/login';</script>")
def viewpaidservices(request):
    loginid=request.session.get('loginid')
    if loginid:
        uob=user.objects.get(loginid=loginid)
        bookings = tbl_booking.objects.get(userid=uob, bookingstatus='Paid')
        payments=tbl_payment.objects.filter(bookingid=bookings)   
        return render(request,'User/viewpaidservices.html',{'payments':payments})   
    else:
        return HttpResponse("<script>alert('Authentication Required Login first');window.location='/guestapp/login';</script>")  

def reportcategorycount(request):
    labels = []
    data = []
    report_data = []

    queryset = (
        tbl_payment.objects
        .filter(paymentstatus="Paid")
        .values("bookingid__serviceid__categoryid__categoryname")
        .annotate(total_services=Count("paymentid"))
        .order_by("-total_services")
    )

    for row in queryset:
        category_name = row["bookingid__serviceid__categoryid__categoryname"]
        total_services = row["total_services"]
        labels.append(category_name)
        data.append(total_services)
        report_data.append({
            "categoryname": category_name,
            "total_services": total_services,
        })

    return render(request, 'User/viewpaidservices.html', {
        'labels': labels,
        'data': data,
        'report_data': report_data,
    })