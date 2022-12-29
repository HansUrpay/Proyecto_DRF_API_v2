"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from payments_2.views import PaymentUserView, ExpiredPaymentView
from services_2.views import ServicesView
from users_2.views import UserCreateView, UserListView

router = DefaultRouter()
router.register(r"services", ServicesView, basename="Services")
router.register(r"payments", PaymentUserView, basename="payments")
router.register(r"expired_payments", ExpiredPaymentView, basename="expired_payments")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/all', UserListView.as_view(), name="users_list"),
    path('users', UserCreateView.as_view(), name="users_create"),
]

urlpatterns += router.urls
