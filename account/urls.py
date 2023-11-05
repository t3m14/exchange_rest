from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include, re_path
from .views import send_otp, verify_otp, create_transaction

urlpatterns = [
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    path("send_otp/", send_otp),
    path("verify_otp/", verify_otp),
    path("transaction/", create_transaction),
]