from django.apps import AppConfig
import os

class HospitalappConfig(AppConfig):
    name = 'HospitalApp'
    #def ready(self):
        #if os.environ.get('RUN_MAIN', None) != 'true':
        #from HospitalApp import MsgSender
        #MsgSender.start()
