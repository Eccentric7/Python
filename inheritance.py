#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 20:27:53 2017

@author: eccentric7
"""

class Parent():
    def __init__(self, last_name, eye_color ):
        print("parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color
    
    def show_info(self):
        print("Last Name -"+self.last_name)
        print("Eye Color -"+self.eye_color)
    
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("child constructor called")
        Parent.__init__(self,last_name, eye_color)
        self.number_of_toys = number_of_toys

#miley_cyrus = Child("cyrus", "blue" , 5)

#billy_cyrus = Parent("Cyrus", "Blue")
miley_cyrus = Child("Cyrus","Green", 6)
#billy_cyrus.show_info()
miley_cyrus.show_info()