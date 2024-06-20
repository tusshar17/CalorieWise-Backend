from django.core.mail import EmailMessage
import os
import random


class Util:
    @staticmethod
    def send_email(data):
        print("========" * 3)
        print(data)
        email = EmailMessage(
            subject=data["subject"],
            body=data["body"],
            from_email=os.environ.get("EMAIL_FROM"),
            to=[data["to_email"]],
        )
        email.send()

    @staticmethod
    def generate_otp():
        otp = random.randint(1000, 9999)
        return otp
