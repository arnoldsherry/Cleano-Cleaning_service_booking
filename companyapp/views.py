from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views
from companyapp.models import tbl_service
from guestapp.models import tbl_company,tbl_login
from adminapp.models import tbl_category, tbl_location, tbl_district
from userapp.models import tbl_booking,tbl_payment,user
from django.db.models import Count,Sum
from django.db.models.functions import TruncMonth
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.
def companyhome(request):
    loginid = request.session.get('loginid')
    revenue_data = []
    months = []
    revenue = []
    total_income = 0
    income_percentage_change = 0
    recent_income_data = []
    
    if loginid:
        try:
            cob = tbl_company.objects.get(loginid=loginid)
            
            # Get revenue data grouped by month for the current company
            queryset = (
                tbl_payment.objects
                .filter(paymentstatus="Paid", bookingid__serviceid__compid=cob)
                .annotate(month=TruncMonth('paymentdate'))
                .values('month')
                .annotate(total_revenue=Sum('totalamount'))
                .order_by('month')
            )
            
            for row in queryset:
                month_name = row['month'].strftime('%b') if row['month'] else ''
                total_revenue = row['total_revenue'] or 0
                months.append(month_name)
                revenue.append(total_revenue)
            
            # Calculate total income (all paid payments)
            total_income_result = tbl_payment.objects.filter(
                paymentstatus="Paid",
                bookingid__serviceid__compid=cob
            ).aggregate(total=Sum('totalamount'))
            total_income = total_income_result['total'] or 0
            
            # Calculate income for current and previous month
            now = timezone.now()
            current_month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            previous_month_end = current_month_start - timedelta(days=1)
            previous_month_start = previous_month_end.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            
            current_month_income = tbl_payment.objects.filter(
                paymentstatus="Paid",
                bookingid__serviceid__compid=cob,
                paymentdate__gte=current_month_start
            ).aggregate(total=Sum('totalamount'))['total'] or 0
            
            previous_month_income = tbl_payment.objects.filter(
                paymentstatus="Paid",
                bookingid__serviceid__compid=cob,
                paymentdate__gte=previous_month_start,
                paymentdate__lt=current_month_start
            ).aggregate(total=Sum('totalamount'))['total'] or 0
            
            # Calculate percentage change
            if previous_month_income > 0:
                income_percentage_change = ((current_month_income - previous_month_income) / previous_month_income) * 100
            elif current_month_income > 0:
                income_percentage_change = 100
            
            # Get last 7 periods for the mini chart
            recent_data = list(queryset[-7:]) if len(queryset) >= 7 else list(queryset)
            recent_income_data = [row['total_revenue'] or 0 for row in recent_data]
            
        except tbl_company.DoesNotExist:
            pass
    
    context = {
        'months': months,
        'revenue': revenue,
        'total_income': total_income,
        'income_percentage_change': round(income_percentage_change, 2),
        'recent_income_data': recent_income_data
    }
    return render(request, 'Company/companyhome.html', context)

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
def reportcategorycount(request):
    labels = []
    data = []
    report_data = []
    loginid=request.session.get('loginid')
    cob=tbl_company.objects.get(loginid=loginid)
    queryset = (
        tbl_payment.objects
        .filter(paymentstatus="Paid",bookingid__serviceid__compid=cob)
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

    return render(request, 'Company/reportcategorycount.html', {
        'labels': labels,
        'data': data,
        'report_data': report_data,
    })

def companyprofile(request):
    loginid = request.session.get('loginid')
    if loginid:
        try:
            company = tbl_company.objects.get(loginid=loginid)
            return render(request, 'Company/companyprofile.html', {'company': company})
        except tbl_company.DoesNotExist:
            return HttpResponse("<script>alert('Company profile not found');window.location='/companyapp/companyhome';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Login first');window.location='/guestapp/login';</script>")

def company_changepassword(request):
    loginid = request.session.get('loginid')
    if loginid:
        if request.method == 'POST':
            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            lob = tbl_login.objects.get(loginid=loginid)

            if lob.password != current_password:
                return HttpResponse("<script>alert('Current password is incorrect');window.location='/companyapp/changepassword';</script>")

            if new_password != confirm_password:
                return HttpResponse("<script>alert('New password and confirm password do not match');window.location='/companyapp/changepassword';</script>")

            lob.password = new_password
            lob.save()
            return HttpResponse("<script>alert('Password changed successfully');window.location='/companyapp/companyprofile';</script>")
        else:
            return render(request, 'Company/changepassword.html')
    else:
        return HttpResponse("<script>alert('Authentication Required Login first');window.location='/guestapp/login';</script>")
def company_logout(request):
    request.session.flush()
    return HttpResponse("<script>alert('Logged out successfully');window.location='/guestapp/login';</script>")
def company_editprofilepagepage(request):
    loginid = request.session.get('loginid')
    if loginid:
            
        company = tbl_company.objects.get(loginid=loginid)
        districts = tbl_district.objects.all()
        locations = tbl_location.objects.all()
        return render(request, 'Company/companyeditprofilepage.html', {'company': company, 'locations': locations, 'districts': districts})
    else:
        return HttpResponse("<script>alert('Authentication Required Login first');window.location='/guestapp/login';</script>")
def company_editprofile(request):
    loginid = request.session.get('loginid')
    if loginid:
        if request.method == 'POST':
            companyname = request.POST.get('companyname')
            username = request.POST.get('username')
            contact = request.POST.get('contact')
            email = request.POST.get('email')
            desc = request.POST.get('desc')
            locationid = request.POST.get('locationid')
            image = request.FILES.get('image')

            cob = tbl_company.objects.get(loginid=loginid)
            cob.compname = companyname
            cob.username = username
            cob.contact = contact
            cob.email = email
            cob.description = desc
            cob.locationid = tbl_location.objects.get(locationid=locationid)
            if image:
                cob.image = image
            cob.save()
            return HttpResponse("<script>alert('Profile updated successfully');window.location='/companyapp/companyprofile';</script>")
        else:
            return HttpResponse("<script>alert('Invalid request method');window.location='/companyapp/companyprofile';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Required Login first');window.location='/guestapp/login';</script>")
def filllocation(request):
    districtid=int(request.POST.get("districtid"))
    location = tbl_location.objects.filter(districtid=districtid).values()
    return JsonResponse(list(location),safe=False)
def reportservicecount(request):
    labels = []
    data = []
    report_data = []
    loginid=request.session.get('loginid')
    cob=tbl_company.objects.get(loginid=loginid)
    queryset = (
        tbl_payment.objects
        .filter(paymentstatus="Paid",bookingid__serviceid__compid=cob)
        .values("bookingid__serviceid__servicename")
        .annotate(total_purchases=Count("paymentid"))
        .order_by("-total_purchases")
    )

    for row in queryset:
        servicename = row["bookingid__serviceid__servicename"]
        total_purchases = row["total_purchases"]
        labels.append(servicename)
        data.append(total_purchases)
        report_data.append({
            "servicename": servicename,
            "total_purchases": total_purchases,
        })

    return render(request, 'Company/reportservicecount.html', {
        'labels': labels,
        'data': data,
        'report_data': report_data,
    })
