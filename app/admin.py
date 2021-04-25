from django.contrib import admin
from .models import Alert,Enquiry
# Register your models here.


class AlertAdmin(admin.ModelAdmin):

    list_display = ["id",'location',"plasma","oxygen","money","others"]



admin.site.register(Enquiry)
admin.site.register(Alert,AlertAdmin)