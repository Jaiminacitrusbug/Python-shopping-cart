from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    # path('home/', views.HomeView.as_view(), name="home"),
    # path('login_action/', views.loginaction),
]
app_name = "apps"

# apps:login

#jaimina@gmail.com /123456