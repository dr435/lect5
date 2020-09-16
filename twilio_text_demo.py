from twilio.rest import Client

account_sid = "AC4bfd4aee33bec11f71080d8c27fbb907"
auth_token = "715f6c4c228b3add595482ecd8d25c19"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="some text message",
                    from_="+12082137624",
                    to="+19738681296")