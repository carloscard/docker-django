from mailjet_rest import Client
from iati_project.settings.base import env


def get_client():
    return Client(auth=(env('MAILJET_API_KEY'), env('MAILJET_API_SECRET')), version='v3.1')


class MailerService:
    def __init__(
        self, mail_from: str, mail_to: str, template_id: int, subject: str, data: dict
    ):
        self.mail_from = mail_from
        self.mail_to = mail_to
        self.template_id = template_id
        self.subject = subject
        self.data = data
        self.name_from = None
        self.name_to = None
        self.cc_to = None

    def with_name_from(self, name_from: str):
        self.name_from = name_from
        return self

    def with_name_to(self, name_to: str):
        self.name_to = name_to
        return self

    def with_cc_to(self, cc_to: str):
        self.cc_to = cc_to
        return self

    def send_email(self):
        data = {
            "Messages": [
                {
                    "From": {"Email": self.mail_from, "Name": self.name_from},
                    "To": [{"Email": self.mail_to, "Name": self.name_to}],
                    "Bcc": [{"Email": self.cc_to, "Name": self.name_to}] if self.cc_to else [],
                    "TemplateID": self.template_id,
                    "TemplateLanguage": True,
                    "Subject": self.subject,
                    "Variables": self.data,
                }
            ]
        }
        return get_client().send.create(data=data)
