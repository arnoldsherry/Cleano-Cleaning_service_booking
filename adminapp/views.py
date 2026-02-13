from itertools import count
import datetime
import json
import os
from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from userapp.models import tbl_booking, tbl_payment
from adminapp.models import tbl_district, tbl_location, tbl_category
from guestapp.models import tbl_company,tbl_login,user
def adminhome(request):
    revenue = tbl_payment.objects.filter(paymentstatus="Paid").aggregate(total_revenue=Count("totalamount"))["total_revenue"] or 0
    total_bookings = tbl_booking.objects.count()
    return render(request, 'Admin/adminhome.html', {'revenue': revenue, 'total_bookings': total_bookings})
def district(request):
    return render(request, 'Admin/district.html')

# Create your views here.
def district_insert(request):
    if request.method == 'POST':
        distname=request.POST.get("dname")
        dob=tbl_district()
        dob.districtname=distname
        if tbl_district.objects.filter(districtname=distname).exists():
            return HttpResponse("<script>alert('District already exists');window.location='/district'</scrpit>")
        else:
            dob.save()
            return HttpResponse("<script>alert('Inserted successfully');window.location='/district'</script>")

def view_district(request):
    district=tbl_district.objects.all()
    return render(request, 'Admin/view_district.html',{'dis':district})
def editdistrict(request,districtid):
    if request.method=='POST':
        dname=request.POST.get("districtname")
        dis=tbl_district.objects.get(districtid=districtid)
        dis.districtname=dname
        dis.save()
        return view_district(request)
    dis=tbl_district.objects.get(districtid=districtid)
    return render(request,'Admin/editdistrict.html',{'dis':dis})
def deletedistrict(request,districtid):
    dob=tbl_district.objects.get(districtid=districtid)
    dob.delete()
    return view_district(request)
    return HttpResponse("<script>alert('Successfully Deleted');window.location='/Admin/view_district/'</script>")

def location(request):
    districts=tbl_district.objects.all()
    return render(request,'Admin/location.html',{'districts':districts})
def location_register(request):
    if request.method == 'POST':
        lname=request.POST.get("lname")
        did=request.POST.get("district")
        lob = tbl_location()
        lob.locationname = lname
        lob.districtid_id = did
        if tbl_location.objects.filter(locationname=lname).exists():
                 return HttpResponse("<script>alert('Location already exists');window.location='/adminapp/location/'</script>")
        else:
            lob.save()
            return HttpResponse("<script>alert('Location inserted successfully');window.location='/adminapp/location/'</script>")

def viewlocation(request):
    districts=tbl_district.objects.all()
    locations=tbl_location.objects.all()
    return render(request, 'Admin/viewlocation.html',{'locs':locations,'districts':districts})  
def filllocation(request):
    districtid = int(request.POST.get("did"))
    location = tbl_location.objects.filter(districtid=districtid).values()
    return JsonResponse(list(location),safe=False)  
def editlocation(request,locationid):
    if request.method=='POST':
        lname=request.POST.get("locationname")
        loc=tbl_location.objects.get(locationid=locationid)
        loc.locationname=lname
        loc.save()
        return viewlocation(request)
    loc=tbl_location.objects.get(locationid=locationid)
    return render(request, 'Admin/editlocation.html',{'dis':loc})

def deletelocation(request,locationid):
    lob=tbl_location.objects.get(locationid=locationid)
    lob.delete()
    return viewlocation(request)

def categories(request):
    return render(request, 'Admin/categories.html')
def category_insert(request):
    if request.method == 'POST':
        cname=request.POST.get("cname")
        cob=tbl_category()
        cob.categoryname=cname
        if tbl_category.objects.filter(categoryname=cname).exists():
            return HttpResponse("<script>alert('Category already exists');window.location='/categories/'</script>")
        else:
            cob.save()
            return HttpResponse("<script>alert('Category inserted successfully');window.location='/categories/'</script>")
def viewcategory(request):
    category=tbl_category.objects.all()
    return render(request, 'Admin/viewcategory.html',{'cat':category})

def editcategory(request,cid):
    if request.method =='POST':
        cname=request.POST.get("categoryname")
        cob=tbl_category.objects.get(categoryid=cid)
        cob.categoryname=cname
        cob.save()
        return viewcategory(request)
    cob=tbl_category.objects.get(categoryid=cid)
    return render(request, 'Admin/editcategory.html',{'cat':cob})
def deletecategory(request,cid):
    cob=tbl_category.objects.get(categoryid=cid)
    cob.delete()
    return viewcategory(request)
def viewcompany(request):
    companies=tbl_company.objects.all()
    return render(request,'Admin/viewcompany.html',{'com':companies})
def deletecompany(request,cid):
    comid=cid
    com_obj=tbl_company.objects.get(compid=comid)
    com_obj.delete()
    return viewcompany(request)
def acceptcompany(request,id):
    logobj=tbl_login.objects.get(loginid=id)
    comobj=tbl_company.objects.get(loginid=logobj)
    comobj.status="Accepted"
    logobj.status="Accepted"
    comobj.save()
    logobj.save()
    return viewcompany(request)
def rejectcompany(request,id):
    logobj=tbl_login.objects.get(loginid=id)
    comobj=tbl_company.objects.get(loginid=logobj)
    comobj.status="Rejected"
    logobj.status="Rejected"
    comobj.save()
    logobj.save()
    return viewcompany(request)
def deletecompany(request,cid):
    logobj=tbl_login.objects.get(loginid=cid)
    comobj=tbl_company.objects.get(loginid=logobj)
    comobj.delete()
    logobj.delete()
    return viewcompany(request)
def customerreport(request):
    customers = user.objects.all()
    return render(request,'Admin/customerreport.html',{'customers':customers})
import csv
def customerreport_excel(request):
    customers = user.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=customers.csv'

    writer = csv.writer(response)
    writer.writerow(['Name','Contact','Email','Username','Password','Location','Login ID'])

    for t in customers:
        writer.writerow([
            t.name,
            t.contact,
            t.email,
            t.username,
            t.password,
            t.locationid.locationname,
            t.loginid.loginid,
        ])

    return response
def datewisepayreport(request):
    report_data = []
    from_date = None
    to_date = None

    if request.method == "POST":
        from_date_str = request.POST.get("fromDate")
        to_date_str = request.POST.get("toDate")

        if from_date_str and to_date_str:
            from_date = datetime.date.fromisoformat(from_date_str)
            to_date = datetime.date.fromisoformat(to_date_str)

            payments = (
                tbl_payment.objects
                .select_related("bookingid__userid", "bookingid__serviceid__compid")
                .filter(
                    paymentstatus="Paid",
                    paymentdate__range=(from_date, to_date)
                )
                .order_by("paymentdate")
            )

            for pay in payments:
                booking = pay.bookingid
                service = booking.serviceid
                company = service.compid
                customer = booking.userid
                report_data.append({
                    "customername": customer.name,
                    "servicename": service.servicename,
                    "companyname": company.compname,
                    "paydate": pay.paymentdate,
                    "payamount": pay.totalamount,
                })

    return render(request, 'Admin/datewisepayreport.html', {
        'report_data': report_data,
        'from_date': from_date,
        'to_date': to_date,
    })
def datewisepayreport_excel(request):
    if request.method == "POST":
        from_date_str = request.POST.get("fromDate")
        to_date_str = request.POST.get("toDate")

        if from_date_str and to_date_str:
            from_date = datetime.date.fromisoformat(from_date_str)
            to_date = datetime.date.fromisoformat(to_date_str)

            payments = (
                tbl_payment.objects
                .select_related("bookingid__userid", "bookingid__serviceid__compid")
                .filter(
                    paymentstatus="Paid",
                    paymentdate__range=(from_date, to_date)
                )
                .order_by("paymentdate")
            )

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=datewise_payments.csv'

            writer = csv.writer(response)
            writer.writerow(['Customer Name', 'Service Name', 'Company Name', 'Payment Date', 'Payment Amount'])

            for pay in payments:
                booking = pay.bookingid
                service = booking.serviceid
                company = service.compid
                customer = booking.userid
                writer.writerow([
                    customer.name,
                    service.servicename,
                    company.compname,
                    pay.paymentdate,
                    pay.totalamount,
                ])

            return response

    return HttpResponse("<script>alert('Invalid request');window.location='/adminapp/datewisepayreport/'</script>")
def datewisebookingreport(request):
    report_data = []
    from_date = None
    to_date = None

    if request.method == "POST":
        from_date_str = request.POST.get("fromDate")
        to_date_str = request.POST.get("toDate")

        if from_date_str and to_date_str:
            from_date = datetime.date.fromisoformat(from_date_str)
            to_date = datetime.date.fromisoformat(to_date_str)

            payments = (
                tbl_payment.objects
                .select_related("bookingid__userid", "bookingid__serviceid__compid")
                .filter(
                    paymentstatus="Paid",
                    bookingid__bookingdate__range=(from_date, to_date)
                )
                .order_by("bookingid__bookingdate")
            )

            for pay in payments:
                booking = pay.bookingid
                service = booking.serviceid
                company = service.compid
                customer = booking.userid
                report_data.append({
                    "customername": customer.name,
                    "servicename": service.servicename,
                    "companyname": company.compname,
                    "bookingdate": booking.bookingdate,
                    "payamount": pay.totalamount,
                })

    return render(request, 'Admin/datewisebookingreport.html', {
        'report_data': report_data,
        'from_date': from_date,
        'to_date': to_date,
    })
def datewisebookingreport_excel(request):
    if request.method == "POST":
        from_date_str = request.POST.get("fromDate")
        to_date_str = request.POST.get("toDate")

        if from_date_str and to_date_str:
            from_date = datetime.date.fromisoformat(from_date_str)
            to_date = datetime.date.fromisoformat(to_date_str)

            payments = (
                tbl_payment.objects
                .select_related("bookingid__userid", "bookingid__serviceid__compid")
                .filter(
                    paymentstatus="Paid",
                    bookingid__bookingdate__range=(from_date, to_date)
                )
                .order_by("bookingid__bookingdate")
            )

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=datewise_payments.csv'

            writer = csv.writer(response)
            writer.writerow(['Customer Name', 'Service Name', 'Company Name', 'Booking Date', 'Payment Amount'])

            for pay in payments:
                booking = pay.bookingid
                service = booking.serviceid
                company = service.compid
                customer = booking.userid
                writer.writerow([
                    customer.name,
                    service.servicename,
                    company.compname,
                    booking.bookingdate,
                    pay.totalamount,
                    
                ])

            return response

    return HttpResponse("<script>alert('Invalid request');window.location='/adminapp/datewisebookingreport/'</script>")
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

    return render(request, 'Admin/reportcategorycount.html', {
        'labels': labels,
        'data': data,
        'report_data': report_data,
    })
def reportcategorycount_piechart(request):
    labels = []
    data = []

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

    return JsonResponse({
        'labels': labels,
        'data': data,
    })