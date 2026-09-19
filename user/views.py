from itertools import count

from django.db.models import Q
from django.shortcuts import render
from . models import  *
from django.http import HttpResponse
from datetime import datetime
from django.db import connection

# Create your views here.
def index(request):
    data=category.objects.all().order_by('-id')[0:12]
    gdata=tbl_slide.objects.all().order_by('id')
    sdata=service_provider.objects.all().order_by('-discount_price')[0:12]
    md={'cdata':data,"servicedata":sdata,'vdata':gdata}
    return render(request,'index.html',md)

def about(request):
    return render(request,'about.html')

def contact(request):
    md={}
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('mobile')
        d=request.POST.get('msg')
        contactus(Name=a,Email=b,Mobile=c,Message=d).save()
        return HttpResponse("<script>('Give me my money..');location.href='/contact/'</script>")
        #md={"a1":a,"email":b,"mobile":c,"message":d}
    return render(request,'contact.html')

def faqs(request):
    return render(request,'faqs.html')
def service(request, service=None):
    sid=request.GET.get('msg')
    sdata=service_provider.objects.all().filter(id=sid)
    services = tbl_service.objects.all().filter(provider_name=sid)
    md={"sdata":sdata,"services":services}

    return  render(request,'service.html',md)
def Registration(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        passwd=request.POST.get('passwd')
        address=request.POST.get('address')
        pincode=request.POST.get('pincode')
        city=request.POST.get('city')
        picture=request.FILES['fu']
        x=tbl_register.objects.all().filter(email=email).count()
        if x==1:
            return HttpResponse("<script>alert('you are alredy register ..');location.href='/Registration/'</script>")
        else:
            tbl_register(name=name,email=email,mobile=mobile,passwd=passwd,address=address,pincode=pincode,city=city,picture=picture).save()
            return HttpResponse("<script>alert('data cannot be change after submission');location.href='/Registration/'</script>")

    return  render(request,'Registration.html')

def login(request):
    if request.method =="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        x=tbl_register.objects.filter(email=email,passwd=password)
        if x.count()==1 :
            request.session['name']=str(x[0].name)
            request.session['picture']=str(x[0].picture)
            request.session['email']=str(x[0].email)
            return HttpResponse("<script>alert('Your are  login..');location.href='/home/'</script>")

        else :
            return HttpResponse("<script>alert('Your not invalid..');location.href='/login/'</script>")

    return render(request,'login.html')

def logout(request):
    if request.session.get('email'):
        del request.session['email']
    return HttpResponse("<script>alert('Logged out');location.href='/login/'</script>")
    return  render(request,'logout.html')

def profile(request):
    user=request.session.get('email')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        passwd = request.POST.get('passwd')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        picture = request.FILES['fu']
        tbl_register(name=name, email=user, mobile=mobile, passwd=passwd, address=address, pincode=pincode,city=city, picture=picture).save()
        return HttpResponse("<script>window.location.href='/profile/'</script>")

    user=request.session.get('email')
    data=tbl_register.objects.all().filter(email=user)
    md={"userinfo":data}
    return render(request,'profile.html',md)

def allservices(request):
    cid=request.GET.get('cid')
    searchdata=request.GET.get('search')
    cdata=category.objects.all().order_by('-id')
    data=""
    if cid is not None:
        data=service_provider.objects.all().filter(service_category=cid)
    elif searchdata is not None:
        data=service_provider.objects.all().filter(Q(service_name__icontains=searchdata)| Q(address__icontains=searchdata) | Q(city__icontains=searchdata) | Q(service_category__category_name__icontains=searchdata))
    else:
        data=service_provider.objects.all().order_by('-id')
    md={"cdata":cdata,"servicedata":data}
    return render(request,'allservices.html',md)
def bookinghistory(request):
    cursor=connection.cursor()
    email = request.session.get('email')
    cursor.execute("select * from user_tbl_booking left join user_service_provider on user_tbl_booking.providerid=user_service_provider.id where user_tbl_booking.email='"+email+"' order by user_tbl_booking.id desc")
    rows=cursor.fetchall()
    md={"data":rows}
    return render(request,'bookinghistory.html',md)
def booknow(request):
    email=request.session.get('email')
    if email is not None:
        if request.method == "POST":
            date = request.POST.get('date')
            time = request.POST.get('time')
            detail = request.POST.get('detail')
            address = request.POST.get('address')
            pincode = request.POST.get('pincode')
            city = request.POST.get('city')
            payment = request.POST.get('payment')
            now=datetime.today()
            provider=request.POST.get('provider')
            tbl_booking(providerid=provider,email=email,date=date,time=time,detail=detail,address=address,city=city,pincode=pincode,payment=payment,reqdate=now,status='pending').save()

            return HttpResponse("<script>alert('Your Booking succesfully ..');location.href='/history/'</script>")
        return render(request,'booknow.html')
    else:
        return HttpResponse("<script>alert('you need to login first to book services');location.href='/booknow/'</script>")
