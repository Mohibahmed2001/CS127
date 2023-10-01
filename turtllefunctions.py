#Mohib Ahmed
#June 23 2023
#mohib.ahmed79@myhunter.cuny.edu
#We fill out two functions

import turtle

def triangle(t, length):
    if length > 10:
        for _ in range(3):
            t.forward(length)
            t.left(120)
        triangle(t, length / 2)

def nestedTriangle(t, length):
    if length > 10:
        for _ in range(3):
            t.forward(length)
            t.left(120)
            nestedTriangle(t, length / 2)

t = turtle.Turtle()
wn = turtle.Screen()
triangle(t, 200)
wn.exitonclick()
