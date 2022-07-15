from django.shortcuts import render
from django.views import View
from .models import User
from django.contrib.auth import authenticate

# Create your views here.
# def login(request):    
#     return render(request, 'apps/login.html')

# def loginaction(request): 
#     print(request)   
#     # return render(request, 'apps/login.html')


class LoginView(View):
    def get(self, request):
        users = User.objects.all()
        for user in users:
            print("user",user.password)
        return render(request, 'apps/login.html')

    def post(self, request):
        user = authenticate(email=request.POST.get("email"), password=request.POST.get("password"))
        if user:
            print("login")
        else:
            print("error")
        return render(request, 'apps/login.html')