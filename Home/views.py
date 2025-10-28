from django.shortcuts import render,HttpResponse
from datetime import datetime
from Home.models import Contact,Sell
#from Home.models import Sell
from django.contrib import messages
from Home.models import Book
#from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    context={
        "variable":"this is sent"
    }
    return render(request,'in.html',context)
    # return HttpResponse("This is home page")

def about(request):
    # return HttpResponse("This is about page")
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')
    # return HttpResponse("This is services")
    
def buy(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, "buy.html", {"books": books})
    # return HttpResponse(request,"This is buys")

#@csrf_exempt   
# def sell(request):
#     if request.method== "POST":
#         bookname = request.POST.get('bookname')
#         sellername = request.POST.get('sellername')
#         email = request.POST.get('email')
#         bookprice = request.POST.get('bookprice')
#         info = request.POST.get('info')
        
#         if bookname and sellername and email and bookprice and info:
#             sell = Sell(bookname=bookname,sellername=sellername, email=email,bookprice=bookprice,info=info)
#             sell.save() #to save v
#             messages.success(request,"message has been send")
            
#         else:
#             print("missing data")
        
        
        
#     return render(request,'sell.html')
#     # return HttpResponse(request,"This is buys")
# def rent(request):
    
#     return render(request,'rent.html')


def sell(request):
    if request.method == "POST":
        bookname = request.POST.get('bookname')
        sellername = request.POST.get('sellername')
        email = request.POST.get('email')
        bookprice = request.POST.get('bookprice')
        info = request.POST.get('info')

        # Check if all required fields are filled
        if bookname and sellername and email and bookprice and info:
            sell = Sell(
                bookname=bookname,
                sellername=sellername,
                email=email,
                bookprice=bookprice,
                info=info
            )
            sell.save()  # Save to the database
            messages.success(request, "Your book has been listed for sale successfully!")
        else:
            messages.error(request, "Please fill out all required fields.")

    return render(request, 'sell.html')

def rent(request):
    rented_books = Book.objects.filter(is_available_for_rent=True)  # Fetch all books
    return render(request, "rent.html", {"books": rented_books})



def contact(request):   
    # json, api, post get put delete , django documentation
    # this is post api
    if request.method == "POST":
        name = request.POST.get('name')   
        email = request.POST.get('email')
        desc = request.POST.get('desc')

        if name and email and desc:
            contact = Contact(name=name, email=email, desc=desc, date=datetime.now())
            contact.save() #to save values in db
            messages.success(request, "Your message has been send.")
            
        else:
            print("Missing Data...")

    return render(request, 'contact.html')

    # return HttpResponse("This is contact page")return render(request,'contact.html')