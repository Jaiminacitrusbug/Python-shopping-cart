from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    # path('login_action/', views.loginaction),
]
app_name = "apps"