from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from adminapp.models import tbl_district,tbl_location
from guestapp.models import user, tbl_login,tbl_company

# Create your views here.
def guesthome(request):
    return render(request, 'Guest/guesthome.html')
def customer(request):
    districts = tbl_district.objects.all()
    locations = tbl_location.objects.all()
    return render(request, 'Guest/customer.html', {'dist': districts,'locs':locations})

def customerreg(request):
    if request.method == "POST":
        lob = tbl_login()
        lob.username = request.POST.get("username")
        lob.password = request.POST.get("password")
        lob.role = "user"

        if tbl_login.objects.filter(username=request.POST.get("username")).exists():
            return HttpResponse("<script>alert('Already Exists..'); window.location='/Guest/customerreg';</script>")
        else:
            lob.save()

            tob = user()
            tob.username = request.POST.get("username")
            tob.name = request.POST.get("name")
            tob.email = request.POST.get("email")
            tob.contact = request.POST.get("contact")
            tob.password = request.POST.get("password")
            tob.locationid = tbl_location.objects.get(locationid=request.POST.get("locationid"))
            tob.loginid = lob
            tob.save()

            return HttpResponse("<script>alert('Successfully registered'); window.location='/Guest/customerreg';</script>")
         
def viewcustomer(request):
    customers=user.objects.all()
    return render(request,'Guest/viewcustomer.html',{'cust':customers})  
def editcustomer(request,customerid):
    if request.method=='POST':
        cname=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("password")
        contact=request.POST.get("contact")
        cob=user.objects.get(userid=customerid)
        cob.username=cname
        cob.password=password
        cob.email=email
        cob.contact=contact
        cob.save()
        return viewcustomer(request)
    cob=user.objects.get(userid=customerid)
    return render(request,'Guest/editcustomer.html',{'cust':cob})
def deletecustomer(request,customerid):
    cob=user.objects.get(userid=customerid)
    cob.delete()
    return viewcustomer(request)
def company(request):
    locations=tbl_location.objects.all()
    return render(request,'Guest/company.html',{'locs':locations})

def companyreg(request):
    if request.method=='POST':
        lob = tbl_login()
        lob.username = request.POST.get("username")
        lob.password = request.POST.get("password")
        lob.role = "company"
        
        if tbl_login.objects.filter(username=request.POST.get("username")).exists():
            return HttpResponse("<script>alert('Already Exists..'); window.location='/guestapp/companyreg';</script>")
        else:
            lob.save()
            com_ob=tbl_company()
            compname=request.POST.get("compname")
            username=request.POST.get("username")
            password=request.POST.get("password")
            email=request.POST.get("email")
            contact=request.POST.get("contact")
            city=request.POST.get("city")
            state=request.POST.get("state")
            street=request.POST.get("street")
            location=request.POST.get("locationid")
            image=request.FILES.get("image")
            com_ob.compname=compname
            com_ob.username=username
            com_ob.password=password
            com_ob.email=email
            com_ob.contact=contact
            com_ob.city=city
            com_ob.state=state
            com_ob.street=street
            com_ob.loginid=lob
            com_ob.locationid=tbl_location.objects.get(locationid=request.POST.get("locationid"))
            com_ob.image=image
            com_ob.description=request.POST.get("description")
            com_ob.save()
            return HttpResponse("<script>alert('Company registered successfully');window.location='/Guest/companyreg';</script>")
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        status = request.POST.get('status')
        role= request.POST.get('role')
        tbl_login.objects.create(
            username=username,
            password=password,
            status=status,
            role=role,
        )

        return redirect('login')

    return render(request, "guest/login.html")
def login_insert(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if tbl_login.objects.filter(
            username=username,
            password=password,
            status='Accepted'     
        ).exists():

            log = tbl_login.objects.get(
                username=username,
                password=password,
                status='Accepted'
            )

            request.session['loginid'] = log.loginid
            role = log.role
            username = log.username
            request.session['username'] = username

            if role == 'admin':
                return redirect('/adminapp/adminhome')
            elif role == 'company':
                return redirect('/companyapp/companyhome')
            elif role == 'user':
                return redirect('/userapp/index')
            else:
                return HttpResponse(
                    "<script>alert('Request not accepted');window.location='/guestapp/login';</script>"
                )
        else:
            return HttpResponse(
                "<script>alert('Invalid credentials or account not approved');window.location='/guestapp/login';</script>"
            )

    return HttpResponse(
        "<script>alert('Invalid request');window.location='/guestapp/login';</script>"
    )