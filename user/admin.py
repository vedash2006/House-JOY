from django.contrib import admin

from . models import *

# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display = ('id','Name','Email','Mobile','Message')

admin.site.register(contactus,contactusAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_picture')

admin.site.register(category,categoryAdmin)

class tbl_registerAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','pincode','city','address','passwd','picture')

admin.site.register(tbl_register,tbl_registerAdmin)

class tbl_slideAdmin(admin.ModelAdmin):
    list_display = ('title','picture','description')

admin.site.register(tbl_slide,tbl_slideAdmin)

class service_providerAdmin(admin.ModelAdmin):
    list_display = ('id','provider_name','provider_picture','per_square','discount_price','service_name','details','availability','provider_mobile','city','address','service_picture','service_category','pincode','added_date')
admin.site.register(service_provider,service_providerAdmin)

class servicesAdmin(admin.ModelAdmin):
    list_display = ('id','service_title','provider_name','description','cost','avg_time','service_pic')
admin.site.register(tbl_service,servicesAdmin)

class tbl_bookingAdmin(admin.ModelAdmin):
    list_display = ('providerid','email','date','time','detail','address','city','pincode','payment','reqdate','status')
admin.site.register(tbl_booking,tbl_bookingAdmin)