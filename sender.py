import os
import smtplib

EMAIL_ADDRESS = os.environ.get("USER_EMAIL")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")
# print(EMAIL_ADDRESS)
# print(EMAIL_PASSWORD)
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'subject what you want'
    body = "text body, mail what you sending"

    msg = f"Subject: {subject}\n\n{body}"

    smtp.sendmail(EMAIL_ADDRESS, "reciver_gmail", msg)
