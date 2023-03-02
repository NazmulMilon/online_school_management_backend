"""Sent mail using Django"""


from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse


def test_mail():
    # email = "ironi@iquantile.com"
    # name = "Imam Hossain Roni"
    # subject = "Subject message"

    send_mail(
        "Meeting reminder",
        "Hello , Please join the meeting tomorrow. \n\n\n\n --Best Regards, \nMd. Milon Sarker",
        'msarker@iquantile.com',
        # settings.EMAIL_HOST_USER,
        ['milon16103373@gmail.com'],
        fail_silently=False
    )

    # return HttpResponse("Done")


