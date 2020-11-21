from twilio.rest import Client
# This belongs to Engigma Rebooted for the HackFest 2019
# Project is Smart Blind Man Stick
account_sid = 'AC3c6c12a72dcee8923300920080247869'
auth_token = '1bf2bd405db1cbdb0713a4b73ed64f2a'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=" Your Friend Rohan is in Need of your help. Visit here: https://locationmagic.org/locate . And enter this code: a609c7235c19dd779729",
                     from_='+12019037583',
                     to='+919458467120'
                 )

print(message.sid)
