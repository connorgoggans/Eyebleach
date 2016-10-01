from twilio.rest import TwilioRestClient


def sendMMS(url):
    account_sid = "AC3a0e74fcece71f0be0b75059fea0ce8a"
    auth_token = "009af745ec6ea0f293cfcfe719300d24"

    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(
        to="+16628015473",
        from_="+16623017018",
        media_url=str(url)
    )

    print(message.sid)
