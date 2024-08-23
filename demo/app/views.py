from django.shortcuts import render
from django.http import JsonResponse
import random
import requests

# Your Fast2SMS API key
API_KEY = 'GeaGOBIQhCN3uukyelLHEwtNzsc9kP9Wlp5VxZcBh1mX1OYF7JNRuldwRmMg'

def index(request):
    return render(request, 'pages/dashboard.html')

def send_otp_to_users(request):
    # List of 150+ user phone numbers
    user_phone_numbers = [
        '6380398016','8903704121'  # Add all numbers here
    ]

    # Generate a random OTP and send to each user
    for phone_number in user_phone_numbers:
        otp = random.randint(100000, 999999)  # Generate a 6-digit OTP

        # Prepare the URL and parameters for the API request
        url = "https://www.fast2sms.com/dev/bulkV2"
        querystring = {
            "authorization": 'GeaGOBIQhCN3uukyelLHEwtNzsc9kP9Wlp5VxZcBh1mX1OYF7JNRuldwRmMg',
            "route": "otp",
            "variables_values": str(otp),
            "flash": "0",
            "numbers": phone_number
        }

        headers = {
            'cache-control': "no-cache"
        }

        # Make the API request to send the OTP
        response = requests.get(url, headers=headers, params=querystring)

        # Log the response from Fast2SMS (optional)
        print(f"Sent OTP {otp} to {phone_number}. Response: {response.text}")

    return JsonResponse({'status': 'success', 'message': 'OTPs sent to all users'})

