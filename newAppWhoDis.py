""" Create a new web application that replies to incoming text messages.
    Reply to those messages with which country the sender's phone number is
    based in, like this:
    "Hi! It looks like your phone number was born in {{ FromCountry }}"
"""

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a customized reply to an incoming text message"""
    country = request.values.get('ToCountry', None)
    
    resp = MessagingResponse()

    resp.message("Hi! It looks like your phone number was born in {}".format(country))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
