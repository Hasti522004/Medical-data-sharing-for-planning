account_sid = 'ACdb78e181bd667fe0528227c305dbe9f4'
auth_token = '9d0e8600a77c6adb85eb476fe868ccf6'
from twilio.rest import Client
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Name : Ayushman Bharat Yojana: Required Document : Family members aadhar card Mobile number Ration card Domicile, etc. Last Date : No Last Date https://mera.pmjay.gov.in/search/login',
    from_='+19259404896',
    to='+919537410667'
)

print(message.sid)