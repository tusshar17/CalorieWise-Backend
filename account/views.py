from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from account.serializers import (
    UserRegisterSerializer,
    UserLogInSerializer,
    UserProfileSerializer,
    UserChangePasswordSerializer,
    SendPasswordResetEmailSerializer,
    UserPasswordResetSerializer,
    VerifyOTPSerializer,
    SendOTPSerializer,
)
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.throttling import AnonRateThrottle
from account.models import User
import datetime


# Genrate token manually
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {"refresh_token": str(refresh), "access_token": str(refresh.access_token)}


class UserRegisterView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [permissions.AllowAny]
    throttle_classes = [AnonRateThrottle]

    def post(self, request, format=None):
        request_data = request.data
        serializer = UserRegisterSerializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(
                {
                    "msg": "Registration successful, proceed to OTP verification",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendOTP(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [permissions.AllowAny]
    throttle_classes = [AnonRateThrottle]

    def post(self, request):
        serializer = SendOTPSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"msg": "OTP sent successfully, please check your email."})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OTPVerification(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [permissions.AllowAny]
    throttle_classes = [AnonRateThrottle]

    def post(self, request):
        print("request data:", request.data)
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            user = User.objects.filter(email=email)[0]
            print(user)
            token = get_token_for_user(user)
            return Response(
                {
                    "msg": "OTP verification successful.",
                    "token": token,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [permissions.AllowAny]
    throttle_classes = [AnonRateThrottle]

    def post(self, request, format=None):
        serializer = UserLogInSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_token_for_user(user)
                return Response(
                    {"msg": "Login successsful", "token": token},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"errors": {"non_field_errors": ["Incorrect login credentials"]}},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        print(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={"user": request.user}
        )
        if serializer.is_valid(raise_exception=True):
            return Response(
                {"msg": "password changed successfully"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]
    throttle_classes = [AnonRateThrottle]

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(
                {"msg": "Password reset link sents. Please check your email."},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]
    throttle_classes = [AnonRateThrottle]

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(
            data=request.data, context={"uid": uid, "token": token}
        )
        if serializer.is_valid(raise_exception=True):
            return Response(
                {"msg": "Password Reset Successful"}, status=status.HTTP_200_OK
            )

        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
