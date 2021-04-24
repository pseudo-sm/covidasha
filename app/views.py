from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
# Create your views here.
import requests
from .models import Alert,Enquiry
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):

    alerts = Alert.objects.all().order_by("-datetime")
    page = request.GET.get('page', 1)
    paginator = Paginator(alerts, 10)
    try:
        alerts = paginator.page(page)
    except PageNotAnInteger:
        alerts = paginator.page(1)
    except EmptyPage:
        alerts = paginator.page(paginator.num_pages)
    return render(request,"index.html",{"alerts":alerts})

@csrf_exempt
def create_alert(request):
    name = request.POST.get("name")
    if request.POST.get("type")=="1":
        want = True
    else:
        want = False
    what = request.POST.get("content")
    location = request.POST.get("location")
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    new_alert = Alert(name=name,want=want,what=what,location=location,phone=phone,email=email)
    new_alert.save()
    class_name = "bg-danger" if want  else  "bg-success"
    sub_text = "Looking for " if want else "Has a"
    return JsonResponse({"id":new_alert.id,"name":new_alert.name,"want":request.POST.get("type"),"what":new_alert.what,"location":new_alert.location,"datetime":new_alert.datetime,"class_name":class_name,"sub_text":sub_text})

@csrf_exempt
def enquire(request):
    print(request.POST)
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    alert_id = request.POST.get("alert_id")
    alert = Alert.objects.get(id=alert_id)
    enquire = Enquiry(name=name,phone=phone,email=email,alert=alert)
    enquire.save()
    body = "{} has taken interest in your alert (Attached at the end of the email). He has shared his phone number and email id with us : \nPhone : {} \n Email : {}. Try contacting, if they are not available give a call to us @8249619206.\n {} \n Location : {} \n Thank You. ".format(name,phone,email,alert.what,alert.location)
    # send_email("New enquiry for your covid alert",body,alert.email)
    send_message(body,alert.phone)
    return JsonResponse(True,safe=False)

def send_email(subject,body,to):
    email_msg = EmailMessage(
            "New Lead",
            body,
            settings.EMAIL_HOST_USER,
            ["admin@cavemendev.com"],
        )
    email_msg.send(fail_silently=False)

import plivo
def send_message(body,to):
    client = plivo.RestClient("MAMWZLODVJNWRKZDG4NJ", "MTNlYmM4MDlhNDgwNjBkODk2MjNkZTMyZTVkODA1")
    response = client.messages.create(
        src='+918249619206',
        dst="+91"+to,
        text=body)
    print(response)

def how_it_works(request):

    return render(request,"how_work.html")