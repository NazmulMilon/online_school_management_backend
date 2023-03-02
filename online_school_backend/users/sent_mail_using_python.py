# import smtplib
# import ssl
#
# smtp_server = "smtp@gmail.com"
# port = 587
# sender_email = "milon16103373@gmail.com"
# password = 123456
# receiver_email = "milonsarker73@gmail.com"
# message = """\
# Subject: Hi there\
#
# This message is sent from Python."""
#
# context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
#     server.ehlo()  # Can be omitted
#     server.starttls(context=context)
#     server.ehlo()  # Can be omitted
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

message = MIMEMultipart()
message["from"] = "Md. Milon Sarker"
message["to"] = "ironi@iquantile.com"
message["subject"] = "This is a test email"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("msarker@iquantile.com", "237milon")
    smtp.send_message(message)
    print("Sent")
