from django.urls import path
from account.views import (
    UserRegisterView,
    UserLoginView,
    UserProfileView,
    UserChangePasswordView,
    SendPasswordResetEmailView,
    UserPasswordResetView,
    OTPVerification,
    SendOTP,
)

urlpatterns = [
    path("send_otp/", SendOTP.as_view(), name="SendOTP"),
    path("verify_otp/", OTPVerification.as_view(), name="OTPVerification"),
    path("register/", UserRegisterView.as_view(), name="UserRegister"),
    path("login/", UserLoginView.as_view(), name="UserLogin"),
    path("profile/", UserProfileView.as_view(), name="UserProfile"),
    path("change_password/", UserChangePasswordView.as_view(), name="ChangePassword"),
    path(
        "send-reset-password-email/",
        SendPasswordResetEmailView.as_view(),
        name="SendResetPasswordEmail",
    ),
    path(
        "reset-password/<uid>/<token>",
        UserPasswordResetView.as_view(),
        name="ResetPassword",
    ),
]
