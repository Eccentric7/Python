#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 02:45:34 2017

@author: bcguwop
#"""

import webbrowser
import time 

total_breaks = 10
break_count = 0

print("This Program started on "+time.ctime())
while(break_count < total_breaks):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=dIC4VSUE7q4")
    break_count = break_count +1 