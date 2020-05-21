import time
import os
from twilio.rest import Client


TWILIO_ACCT = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE = os.getenv('TWILIO_PHONE')


client = Client(TWILIO_ACCT, TWILIO_AUTH)


def leave_voicemail(to: str, msg: str) -> None:
    call = client.calls.create(
        twiml=f'<Response><Say>{msg}</Say><Hangup/></Response>',
        machine_detection='DetectMessageEnd',
        to=to,
        from_=TWILIO_PHONE
    )
    sid = call.sid
    while True:
        call = client.calls(sid).fetch()
        if call.status in ['canceled', 'completed', 'busy', 'no-answer', 'failed']:
            break
        time.sleep(1)
