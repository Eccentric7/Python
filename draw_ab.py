#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 22:01:02 2017

@author: eccentric7
"""

import turtle 

def draw_a(fu):  
    fu.down()
    fu.backward(90)
    fu.left(90)
    fu.down()
    fu.backward(120)
    fu.forward(60)
    fu.right(90)
    fu.down
    fu.forward(90)
    fu.right(90)
    fu.forward(60)
    fu.backward(120)
    
def draw_b(t):
    t.up()
    t.forward(20)
    t.down()
    t.forward(100)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(60)
    t.backward(60)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(120)
    
          
    
def draw_ab():
    window = turtle.Screen()
    window.bgcolor("black")
   
    fu = turtle.Turtle()
    fu.shape("turtle")
    fu.speed("slowest")
    fu.color("red")
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed("slow")
    t.color("green")
    draw_a(fu)
    draw_b(t)
    
draw_ab()

turtle.mainloop()