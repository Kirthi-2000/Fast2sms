from django.urls import path
from .views import send_otp_to_users

urlpatterns = [
    path('send-otp/', send_otp_to_users, name='send_otp'),
]
