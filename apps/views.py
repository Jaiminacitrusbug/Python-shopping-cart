from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from shoppingCart.forms import OrderForm
from .models import OrderProduct, Product, User, Order
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
        forms = OrderForm()
        context={}
        if user.role=='admin':
            order=  Order.objects.all()
            context={
            "order":order,"forms":forms
            }
        else:
            order= Order.objects.filter(user_email=user.email) 
            context={
            "order":order
            }  
                        
        print("order............",order)
        # context=order
        
        return render(request, self.template_name,context)
    
    def post(self, request):
        if 'Add' in request.POST:
            forms = OrderForm()

        else:
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
            orderproduct =OrderProduct.objects.create(
                price=price,
                # product=Product.objects.get(id=product) ,
                quantity=quatities,
                product=Product.objects.filter(id=product).get("id")
            )
            # orderproduct.product.set(Product.objects.filter(id=product))
            orders.product.set(Product.objects.filter(id=product))
            print("Order",Order.objects.all())        
            return redirect('apps:home')
        

class CalculatePriceView(View):
    def get(self, request):  
        id= request.GET.get("id")
        qty= request.GET.get("quantity")
        product = Product.objects.get(id=id)
        total= product.price*int(qty)
        disc_price=0
        if product.discount_type==product.per:
            disc_price= total- ((total*product.discount_value)/100)
        else:
            disc_price= total- product.discount_value
        # product= Product()
        # total_price= product.getPrice(id,qty)
        print("total-----------",disc_price)
        return JsonResponse({"total":disc_price})
        
   
   
        