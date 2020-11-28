from django.shortcuts import render, HttpResponse,redirect
from .forms import ContactForm
from .models import User
import requests
import json

# Create your views here.

def loginPage(request):
    return render(request, 'login.html')

def logOutPage(request):
    return render(request, 'login.html')


def ContactPage(request):
    if request.method=="POST":
        Name=request.POST['name']
        Email=request.POST['email']
        Phone=request.POST['phone']
        Message =request.POST['message']
        
        user=User(Name=Name, Email=Email, Phone=Phone, Message=Message)
        user.save()

#Rcaptcha Stuff
        clientkey = request.POST["g-recaptcha-response"] 
        secretkey = "6LcmXvAZAAAAAMLgkwDSPDD9AmJuZK_biJ3X4Kir"
        captcha_data = {
            'secret':secretkey,
            'response': clientkey
        }
        r= requests.post("https://www.google.com/recaptcha/api/siteverify", data = captcha_data)
        response = json.loads(r.text)
        verify = response["success"]
        if verify:
            return HttpResponse('<script> alert("Form Submitted Successfully")</script>')
        else:
            return HttpResponse('<script> alert("Form Submission Failed")</script>')
        
        

    return render(request, 'contact.html')


def Analytics(request):
    return render(request, 'Analytics.html')