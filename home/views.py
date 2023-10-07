from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("This is home page")
def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is about page")
def contact(request):
    if request.method == "POST":   #here we define that if we use POST method than execute this if block else just render and return the page.
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        phone=request.POST.get('phone')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,"Your message has been successfully sent.!") 
    return render(request,'contact.html')
    # return HttpResponse("This is contact page")
def services(request):
    return render(request,'services.html')
    # return HttpResponse("This is services page")