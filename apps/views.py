import email
from django.shortcuts import render
from django.views import View
from .models import User, Order
from django.contrib.auth import authenticate

# Create your views here.
# def login(request):    
#     return render(request, 'apps/login.html')

# def loginaction(request): 
#     print(request)   
#     # return render(request, 'apps/login.html')


class LoginView(View):
    template_name='apps/home.html'
    def get(self, request):
        users = User.objects.all()
        for user in users:
            print("user",user.password)
        return render(request, 'apps/login.html')

    def post(self, request):
        user = authenticate(email=request.POST.get("email"), password=request.POST.get("password"))
        if user:
            user = User.objects.get(email=request.POST.get("email"))
            # order=[]
            print(user.role)
            if user.role=='admin':
                order=  Order.objects.all()
            else:
                order=  Order.objects.filter(user_email=request.POST.get("email"))               
            print("order............",order)
            context=order
            return render(request, self.template_name,{"order":context})
        else:
            print("error")

# class HomeView(View):
#     def get(self, request):      
#         return render(request, 'apps/home.html')

   
        