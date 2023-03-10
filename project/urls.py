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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import re_path
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Pagos",
        default_version='v2',
        description="En el proyecto se desarrolla una API de pagos",
        terms_of_service="https://github.com/HansUrpay",
        contact=openapi.Contact(email="hansurpayh@gmail.com"),
        license=openapi.License(name="BSD License"),
),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r"services", ServicesView, basename="Services")
router.register(r"payments", PaymentUserView, basename="payments")
router.register(r"expired_payments", ExpiredPaymentView, basename="expired_payments")

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('users_2.urls')),
    path('users/all', UserListView.as_view(), name="users_list"),
    path('users', UserCreateView.as_view(), name="users_create"),

    # Documentacion
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh/", TokenRefreshView.as_view(),  name="refresh_token"),
]

urlpatterns += router.urls
