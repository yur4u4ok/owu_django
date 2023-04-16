import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from configs.celery import app
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken


class EmailService:

    @staticmethod
    @app.task
    def __send_email(to: str, template_name: str, context: dict, subject=''):
        template = get_template(template_name)
        content = template.render(context)
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get('EMAIL_HOST_USER'),
                                     to=[to])

        msg.attach_alternative(content, 'text/html')

        msg.send()

    @classmethod
    def register_email(cls, user):
        token = JWTService.create_token(user, ActivateToken)
        url = f"http://localhost:3000/activate/{token}"
        cls.__send_email.delay(user.email, "email_template.html", {"name": user.profile.name, "url": url}, "Register")

    @classmethod
    def recovery_password_email(cls, user):
        token = JWTService.create_token(user, RecoveryToken)
        url = f"http://localhost:3000/recovery/{token}"
        cls.__send_email(user.email, "recovery_password_email.html", {"name": user.profile.name, "url": url},
                         "Recovery Password")
