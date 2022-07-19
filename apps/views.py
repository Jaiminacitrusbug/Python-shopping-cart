from django.utils import timezone
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from shoppingCart.forms import OrderForm
from .models import Product, User, Order
from datetime import datetime
from django.contrib.auth import authenticate,login
print("product-----------------------------------",tuple(Product.objects.values_list('id', 'name')))

# Create your views here.
# def login(request):    
#     return render(request, 'apps/login.html')

# def loginaction(request): 
#     print(request)   
#     # return render(request, 'apps/login.html')


class LoginView(View):
   
    def get(self, request):     
        return render(request, 'apps/login.html')

    def post(self, request):
        user = authenticate(email=request.POST.get("email"), password=request.POST.get("password"))
        if user:
            login(request,user)
            return redirect('apps:home')          
        else:
            print("error")

class HomeView(View):
    template_name='apps/home.html'
    def get(self, request):      
        user = request.user
            # order=[]
        print(user.role)
        if user.role=='admin':
            order=  Order.objects.all()
        else:
            order=  Order.objects.filter(user_email=user.email)               
        print("order............",order)
        context=order
        forms = OrderForm()
        return render(request, self.template_name,{"order":context,"forms":forms})
    
    def post(self, request):
        product=request.POST.get("product")
        user_email=request.POST.get("user_email")
        quatities=request.POST.get("quatities")
        price=request.POST.get("price")
        orders=Order.objects.create(
            user_email=user_email,
            # product=Product.objects.get(id=product) ,
            created_date=datetime.today(),
            price=price
        )
        orders.product.set(Product.objects.filter(id=product))
        print("Order",Order.objects.all())        
        return redirect('apps:home')  

   
        