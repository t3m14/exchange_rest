from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .helpers import send_otp_to_phone
from .models import User, Transaction
@api_view(['POST'])
def send_otp(request):
    data = request.data
    
    if data.get('phone') is None:
        return Response({
            "status": 400,
            "message" : 'key phone is required'
        })
    if data.get('password') is None:
        return Response({
            "status": 400,
            "message" : 'key password is required'
        })
    user = User.objects.create(
        phone = data.get("phone"),
        otp = send_otp_to_phone(data.get("phone"))
        )
    user.set_password = data.get("set_password")
    user.save()
    return Response({
        "status" : 200,
        "message" : "Otp sent"
    })
@api_view(['POST'])
def verify_otp(request):
    data = request.data
    
    if data.get('phone') is None:
        return Response({
            "status": 400,
            "message" : 'key phone is required'
        })
    if data.get('password') is None:
        return Response({
            "status": 400,
            "message" : 'key password is required'
        })
    try:    
        user_obj = User.objects.get(phone = data.get("phone"))
    except Exception as e:
        return Response({
            "status": 400,
            "message" : 'Invalid phone number'
        })
    if user_obj.otp == data.get("otp"):
        user_obj.is_phone_verified = True
        user_obj.save()
        return Response({
            'status' : 200,
            'message' : 'Otp matched'
        })
    return Response({
        'status' : 400,
        'message' : 'Invalid otp'
    })
@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def create_transaction(request):
    data = request.data
    if data.get('wallet') is None:
        return Response({
            "status": 400,
            "message" : 'key wallet is required'
        })
    if data.get('rdw') is None:
        return Response({
            "status": 400,
            "message" : 'key password is required'
        })
    transaction = Transaction.objects.create(
        wallet = data.get("wallet"),
        rdw = data.get("rdw")
        )
    transaction.save()
    return Response({
        "status":201,
        "message":"Transaction created"
    })