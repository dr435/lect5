from twilio.rest import Client
import os

account_sid = os.environ(TWILIO_ACCT_SID)
auth_token = os.environ(TWILIO_AUTH_TOKEN)

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="some text message",
                    from_="+12082137624",
                    to="+19738681296")