from django.shortcuts import render
from django.http import HttpResponse
from adminapp.models import tbl_category, tbl_district, tbl_location
from companyapp.models import tbl_service
from guestapp.models import tbl_login,user,tbl_company
from userapp.models import tbl_booking
from django.http import JsonResponse
from userapp.models import tbl_payment,tbl_credit
from datetime import datetime
from django.db.models import Count, Sum  
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
        pd=datetime.now().date()
        return render(request,'User/paymentpage.html',{'booking':booking,'pd':pd})
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
        bookings = tbl_booking.objects.filter(userid=uob, bookingstatus='Paid')
        payments=tbl_payment.objects.filter(bookingid__in=bookings)   
        return render(request,'User/viewpaidservices.html',{'payments':payments})   
    else:
        return HttpResponse("<script>alert('Authentication Required Login first');window.location='/guestapp/login';</script>")  

def reportcategorycount(request):
    labels = []
    data = []
    report_data = []
    loginid=request.session.get('loginid')
    uob=user.objects.get(loginid=loginid)
    queryset = (
        tbl_payment.objects
        .filter(paymentstatus="Paid",bookingid__userid=uob)
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

    return render(request, 'User/reportcategorycount.html', {
        'labels': labels,
        'data': data,
        'report_data': report_data,
    })
def addcleanocredit(request):
    loginid=request.session.get('loginid')
    cr_objs=tbl_credit.objects.filter(userid__loginid=loginid)
    return render(request,'User/addcleanocredit.html',{'cr_objs':cr_objs})
def add_credit(request):
    loginid=request.session.get('loginid')
    if loginid:
        if request.method=='POST':
            creditamount=int(request.POST.get("creditamount"))
            uob=user.objects.get(loginid=loginid)
            userid=uob.userid
            # Get or create a single credit object for the user
            cr_obj, created = tbl_credit.objects.get_or_create(userid=user.objects.get(userid=userid))
            # Increment the credit amount
            cr_obj.creditamount = cr_obj.creditamount + creditamount
            cr_obj.save()
            return HttpResponse("<script>alert('Balance Added Successfully');window.location='/userapp/addcleanocredit';</script>")
        else:
            return HttpResponse("<script>alert('Invalid Request Method');window.location='/userapp/addcleanocredit';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Login first');window.location='/guestapp/login';</script>")
def paywithcreditbalance(request,bookingid):
    loginid=request.session.get('loginid')
    if loginid:
        uob=user.objects.get(loginid=loginid)
        userid=uob.userid
        uob2=user.objects.get(userid=userid)
        cr_obj=tbl_credit.objects.get(userid=uob2)
        booking=tbl_booking.objects.get(bookingid=bookingid, userid=uob)
        totalamount=request.POST.get("totalamount")
        tot=int(totalamount)
        if cr_obj.creditamount >= (tot):
            cr_obj.creditamount = cr_obj.creditamount-(tot)
            cr_obj.save()
            pob=tbl_payment()
            pob.bookingid=tbl_booking.objects.get(bookingid=bookingid)
            pob.totalamount=totalamount
            pob.paymentstatus="Paid"
            booking.bookingstatus='Paid'
            pob.paymentdate = datetime.now().date()
            pob.save()
            booking.save()
            return HttpResponse("<script>alert('Payment Successful');window.location='/userapp/mybookings';</script>")
        else:
            return HttpResponse("<script>alert('Insufficient Credit Balance');window.location='/userapp/mybookings';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Login first');window.location='/guestapp/login';</script>")

def viewprofile(request):
    loginid=request.session.get('loginid')
    if loginid:
        uob=user.objects.get(loginid=loginid)
        
        # Get statistics
        total_bookings = tbl_booking.objects.filter(userid=uob).count()
        paid_bookings = tbl_booking.objects.filter(userid=uob, bookingstatus='Paid')
        paid_services = paid_bookings.count()
        pending_bookings = tbl_booking.objects.filter(userid=uob).exclude(bookingstatus='Paid').count()
        
        # Calculate total spent
        total_spent = tbl_payment.objects.filter(
            bookingid__userid=uob, 
            paymentstatus='Paid'
        ).aggregate(total=Sum('totalamount'))['total'] or 0
        
        # Get credit balance
        try:
            credit_obj = tbl_credit.objects.get(userid=uob)
            credit_balance = credit_obj.creditamount
        except tbl_credit.DoesNotExist:
            credit_balance = 0
        
        context = {
            'user': uob,
            'total_bookings': total_bookings,
            'paid_services': paid_services,
            'pending_bookings': pending_bookings,
            'total_spent': total_spent,
            'credit_balance': credit_balance,
        }
        
        return render(request, 'User/viewprofile.html', context)
    else:
        return HttpResponse("<script>alert('Authentication Required Login first');window.location='/guestapp/login';</script>")

def reportservicecount(request):
    labels = []
    data = []
    report_data = []
    loginid=request.session.get('loginid')
    uob=user.objects.get(loginid=loginid)
    queryset = (
        tbl_payment.objects
        .filter(paymentstatus="Paid",bookingid__userid=uob)
        .values("bookingid__serviceid__servicename")
        .annotate(totalamount=Sum("totalamount"))
        .order_by("-totalamount")
    )

    for row in queryset:
        service_name = row["bookingid__serviceid__servicename"]
        totalamount = row["totalamount"]
        labels.append(service_name)
        data.append(totalamount)
        report_data.append({
            "servicename": service_name,
            "totalamountspend": totalamount,
        })

    return render(request, 'User/reportservicecount.html', {
        'labels': labels,
        'data': data,
        'report_data': report_data,
    })
def changepassword(request):
    loginid=request.session.get('loginid')
    if loginid:
        if request.method == 'POST':
            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            uob = user.objects.get(loginid=loginid)

            if uob.password != current_password:
                return HttpResponse("<script>alert('Current password is incorrect');window.location='/userapp/changepassword';</script>")

            if new_password != confirm_password:
                return HttpResponse("<script>alert('New password and confirm password do not match');window.location='/userapp/changepassword';</script>")

            uob.password = new_password
            uob.save()
            return HttpResponse("<script>alert('Password changed successfully');window.location='/userapp/viewprofile';</script>")
        else:
            return render(request, 'User/changepassword.html')
    else:
        return HttpResponse("<script>alert('Authentication Required Login first');window.location='/guestapp/login';</script>")
def logout(request):
    request.session.flush()
    return HttpResponse("<script>alert('Logged out successfully');window.location='/guestapp/login';</script>")
def editprofilepage(request):
    loginid=request.session.get('loginid')
    if loginid:
        uob=user.objects.get(loginid=loginid)
        districts=tbl_district.objects.all()
        locations=tbl_location.objects.all()
        return render(request,'User/editprofilepage.html',{'user':uob,'districts':districts,'locations':locations})
    else:
        return HttpResponse("<script>alert('Authentication Required Login first');window.location='/guestapp/login';</script>")
def editprofile(request):
    loginid=request.session.get('loginid')
    if loginid:
        if request.method=='POST':
            name=request.POST.get("name")
            username=request.POST.get("username")
            contact=request.POST.get("contact")
            email=request.POST.get("email")
            locationid=request.POST.get("locationid")
            uob=user.objects.get(loginid=loginid)
            uob.name=name
            uob.username=username
            uob.contact=contact
            uob.email=email
            uob.locationid=locationid
            uob.save()
            return HttpResponse("<script>alert('Profile Updated Successfully');window.location='/userapp/viewprofile';</script>")
        else:
            return HttpResponse("<script>alert('Invalid Request Method');window.location='/userapp/editprofilepage';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Login first');window.location='/guestapp/login';</script>")
def filllocation(request):
    districtid = int(request.POST.get("districtid"))
    locations = tbl_location.objects.filter(districtid=districtid).values()
    return JsonResponse(list(locations),safe=False)
def fillservicesbycompany(request):
    companyid=int(request.POST.get("companyid"))
    services=tbl_service.objects.filter(compid=companyid).values()
    return JsonResponse(list(services),safe=False)
def searchservicesbycompany(request):
    company=tbl_company.objects.filter(status='Accepted')
    return render(request,'User/searchservicebycompany.html',{'com':company})

