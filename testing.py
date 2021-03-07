# import smtplib
#
# gmail_user = 'jeremycurmi13@gmail.com'
# gmail_password = 'airjordan23'
#
#
# sent_from = gmail_user
# to = ["jeremycurmi13@gmail.com"] # get from contacts
# subject = "ai testing"
# body = "testing purposes"
#
# email_text = """
# From:{}
# To:{}
# Subject:{}
#
# {}
# """.format(sent_from, ", ".join(to), subject, body)
# print(email_text)
#
# try:
#     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server.ehlo()
#     server.login(gmail_user, gmail_password)
#     server.sendmail(sent_from, to, email_text)
#     server.close()
#     print('Email sent!')
# except:
#     print('Something went wrong...')


# import os
# from decouple import config
# from twilio.rest import Client
#
# MY_PHONE_NUMBER = config('MY_PHONE_NUMBER')
# ACCOUNT_SID = config("ACCOUNT_SID")
# AUTH_TOKEN = config("AUTH_TOKEN")
#
# # account_sid = ""
# # auth_token = ""
# #
# from_whatsapp_number = "whatsapp:+14155238886"
# to_whatsapp_number="whatsapp:" + MY_PHONE_NUMBER
#
# client = Client(ACCOUNT_SID, AUTH_TOKEN)
# client.messages.create(body="Ahoy world!",from_=from_whatsapp_number,to = to_whatsapp_number)
import requests
import json

url = "https://apic.go.com.mt/go/b2b/api/messaging/v1/sms"
payload = {
    "from": "35679081894",
    "to": [
     {
     "msisdn": "35679081894"
     }
    ],
    "body": "Sample text message.",
    "transactionReference": "",
    "logDescription": "SMS reminder sent to client.",
    "logReason": "SMS Reminder",
    "udfs": [
     {
     "key": "application-name",
     "value": "AppointmentScheduler"
     }
    ]
 }
response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
