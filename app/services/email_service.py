# email_service.py
from builtins import ValueError, dict, str
from settings.config import settings
from app.utils.smtp_connection import SMTPClient
from app.utils.template_manager import TemplateManager
from app.models.user_model import User
import logging

class EmailService:
    def __init__(self, template_manager: TemplateManager):
        try:
            self.smtp_client = SMTPClient(
                server=settings.smtp_server,
                port=settings.smtp_port,
                username=settings.smtp_username,
                password=settings.smtp_password
            )
            self.template_manager = template_manager
        except Exception as e:
            logging.error(f"Failed to initialize EmailService: {str(e)}")
            # Don't raise the exception, allow the service to initialize without email capability
            self.smtp_client = None
            self.template_manager = template_manager

    async def send_user_email(self, user_data: dict, email_type: str):
        """Send an email to a user."""
        try:
            if not self.smtp_client:
                logging.warning("SMTP client not initialized, skipping email send")
                return

            subject_map = {
                'email_verification': "Verify Your Account",
                'password_reset': "Password Reset Instructions",
                'account_locked': "Account Locked Notification"
            }

            if email_type not in subject_map:
                raise ValueError("Invalid email type")

            html_content = self.template_manager.render_template(email_type, **user_data)
            self.smtp_client.send_email(
                subject=subject_map[email_type],
                html_content=html_content,
                recipient=user_data['email']
            )
        except Exception as e:
            logging.error(f"Failed to send email: {str(e)}")
            # Don't raise the exception, allow registration to continue even if email fails

    async def send_verification_email(self, user: User):
        verification_url = f"{settings.server_base_url}verify-email/{user.id}/{user.verification_token}"
        await self.send_user_email({
            "name": user.first_name,
            "verification_url": verification_url,
            "email": user.email
        }, 'email_verification')