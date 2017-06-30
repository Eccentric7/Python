#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 18:07:26 2017

@author: bcguwop
"""
import turtle 

def draw_3squares(fu):
    for i in range(4):
        fu.forward(100)
        fu.right(90)
        
#    fu.backward(1)
#    
#    for i in range(4):
#        fu.backward(100)
#        fu.left(90)    
#
#    fu.backward(100)
#    
#    for i in range(4):
#        fu.backward(100)
#        fu.left(90)  
#def triangle(paul):
#       for i in range(3):
#        paul.forward(50)
#        paul.left(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
 
    fu = turtle.Turtle()
    fu.shape("turtle")
    fu.speed("fastest")
    fu.color("red")
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("blue")
    for i in range(40):
            draw_3squares(fu)
            fu.right(10)
    angie.circle(100)
    paul = turtle.Turtle()
    paul.shape("turtle")
    paul.color("black")
    paul.speed("slowest")
    triangle(paul)
 
draw_art()


    

turtle.mainloop()
