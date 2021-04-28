from django.contrib import admin
from .models import Alert,Enquiry, FoodOrder
# Register your models here.


class AlertAdmin(admin.ModelAdmin):

    list_display = ["id",'location',"plasma","oxygen","money","others"]

class EnquiryAdmin(admin.ModelAdmin):

    list_display = ["id",'alert',"name","phone","datetime"]

class OrderAdmin(admin.ModelAdmin):

    list_display = ["id","name","phone","period","address","datetime"]



admin.site.register(Enquiry,EnquiryAdmin)
admin.site.register(FoodOrder,OrderAdmin)
admin.site.register(Alert,AlertAdmin)