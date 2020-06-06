import os

from sendgrid import sendgrid
from sendgrid.helpers.mail import *


def send_email(filled_subject, body, sender_mail):
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    sg.client.mail.send.post(request_body=Mail(sender_mail, To(os.environ.get('MAIL_USERNAME')),
                                               filled_subject, PlainTextContent(body)).get())
