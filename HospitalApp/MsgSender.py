from apscheduler.schedulers.background import BackgroundScheduler
from HospitalApp.models.PatientModel import tbl_patient_information
import os
from twilio.rest import Client
from django.conf import settings
import atexit
from sms import send_sms
def start():
    print("call fun")
    
    
    scheduler = BackgroundScheduler()
    
    scheduler.add_job(SendMessage,'interval',minutes=500)
    
    scheduler.start()

   
    
    
    atexit.register(lambda: scheduler.shutdown())


def SendMessage():

    # account_sid = 'AC837f6c6c9027b4458eb33cd8d10948d7'
    # auth_token = '549867ad8bda64aca525f3edef747612'
    # client = Client(account_sid, auth_token)

    # message = client.messages \
    #             .create(
    #                  body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    #                  from_='+917573864415',
    #                  to='+919879735128'
    #              )

    # print(message.sid)
    # from twilio.rest import Client 
 
    # account_sid = 'ACb0baa9425573aee4cd07349a3d75a1dc' 
    # auth_token = 'fa605f7ccfdd6c5406c8c03bf02b140f' 
    # client = Client(account_sid, auth_token) 
    
    # message = client.messages.create(     
    #                             body="Join Earth's mightiest heroes. Like Kevin Bacon.",    
    #                             from_='+917573864415',
    #                             to='9054504415' 
    #                       ) 
 
    print("class")