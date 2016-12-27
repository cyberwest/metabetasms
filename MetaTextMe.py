_author_ = "Dr James Morris"

#! /usr/bin/python

from twilio.rest import TwilioRestClient
# put your own credentials here
ACCOUNT_SID = 'ACe5a39e9215b07ae0f5864d82a4bd123b'
AUTH_TOKEN = '637c585ef2c0ef32b1d31805f711d79d'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to = '+447787124014',
    from_ = '+441752395189',
    body = 'Help! I am stuck in this smartphone!',
)