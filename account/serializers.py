from rest_framework import serializers
from account.models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from account.utils import Util


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        fields = ["email", "name", "password", "confirm_password", "tc"]
        extra_kwargs = {"password": {"write_only": True}}

    # validate password and confirm password
    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError("Passwords not matching")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLogInSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ["email", "password"]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "name"]


class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )

    class Meta:
        fields = ["password", "confirm_password"]

    # validate password and confirm password
    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        user = self.context.get("user")

        if password != confirm_password:
            raise serializers.ValidationError("Passwords not matching")
        user.set_password(password)
        user.save()
        return attrs


class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ["email"]

    def validate(self, attrs):
        email = attrs.get("email")
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print("encoded uid:", uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print("password reset token:", token)
            reset_link = (
                "http://127.0.0.1:8000/api/user/reset-password/" + uid + "/" + token
            )
            print("password reset link:", reset_link)

            # send email
            data = {
                "subject": "CalorieWise | Password Reset Link",
                "body": "Here is your password reset link: \n {} \n Note: this link is valid for 10 minutes. ".format(
                    reset_link
                ),
                "to_email": user.email,
            }
            Util.send_email(data)

            print("email sent")

            return attrs
        else:
            raise serializers.ValidationError("This email is not registered.")


class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )

    class Meta:
        fields = ["password", "confirm_password"]

    # validate password and confirm password
    def validate(self, attrs):
        try:
            password = attrs.get("password")
            confirm_password = attrs.get("confirm_password")
            uid = self.context.get("uid")
            token = self.context.get("token")

            if password != confirm_password:
                raise serializers.ValidationError("Passwords not matching")

            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError("Token invalid")

            user.set_password(password)
            user.save()
            return attrs

        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError("Token invalid")
