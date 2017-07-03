#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 23:33:48 2017

@author: eccentric7
"""

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc5df36140cc611a8a728077627730218"
# Your Auth Token from twilio.com/console
auth_token  = "fdebd8414f5d310c29cedabaf7038b9f"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14244001897", 
    from_="+17472290982",
    body="Nigga we made it!")

print(message.sid)