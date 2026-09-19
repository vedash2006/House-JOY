from tkinter.constants import CASCADE
from tinymce.models import HTMLField
from django.db import models
from django.db.models import TextField, IntegerField


# Create your models here.
class contactus(models.Model):
    Name=models.CharField(max_length=50,null=True)
    Email=models.CharField(max_length=50,null=True)
    Mobile=models.CharField(max_length=12,null=True)
    Message=models.TextField(null=True)

class category(models.Model):
    category_name=models.CharField(max_length=50,null=True)
    category_picture=models.ImageField(upload_to='static/category/',null=True)
    def __str__(self):
        return self.category_name

class tbl_register(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50,primary_key=True)
    mobile = models.CharField(max_length=16, null=True)
    pincode = models.IntegerField(null=True)
    city = models.CharField(max_length=50,null=True)
    address = models.TextField(null=True)
    passwd = models.CharField(max_length=25,null=True)
    picture = models.ImageField(upload_to='static/profilepicture/',null=True)


class tbl_slide(models.Model):
      title= models.CharField(max_length=50, null=True)
      picture = models.ImageField(upload_to='static/slider/', null=True)
      description = models.TextField(null=True)

class service_provider(models.Model):
    provider_name = models.CharField(max_length=50,null=True)
    provider_picture = models.ImageField(upload_to='static/provider/',null=True)
    per_square = models.FloatField()
    discount_price = models.FloatField()
    service_name = models.CharField(max_length=200,null=True)
    details = models.TextField(null=True)
    availability = HTMLField(null=True)
    provider_mobile = models.CharField(max_length=20,null=True)
    city = models.TextField(max_length=40,null=True)
    address = TextField(null=True)
    service_picture = models.ImageField(upload_to='static/service/',null=True)
    service_category = models.ForeignKey(category,on_delete=models.CASCADE)
    pincode = models.IntegerField(null=True)
    added_date = models.DateField(null=True)
    def __str__(self):
        return self.provider_name

class tbl_service(models.Model):
    service_title = models.TextField(max_length=30,null=True)
    provider_name = models.ForeignKey(service_provider,on_delete=models.CASCADE)
    description = models.TextField(null=True)
    cost = models.IntegerField()
    avg_time = models.TextField(null=True)
    service_pic = models.ImageField(upload_to='static/servicepic/',null=True)

class tbl_booking(models.Model):
    providerid=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    date=models.DateField(null=True)
    time=models.CharField(max_length=50,null=True)
    detail=models.TextField(null=True)
    address=models.TextField(null=True)
    city=models.CharField(max_length=50,null=True)
    pincode=models.IntegerField(null=True)
    payment=models.IntegerField(null=True)
    reqdate=models.CharField(max_length=50,null=True)
    status=models.CharField(max_length=50,null=True)



