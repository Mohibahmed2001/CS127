#Name: Mohib Ahmed
#Email: mohib.ahmed79@myhunter.cuny.edu
#Date: September 11, 2022
#This program draws a fan by implenting the pseudocode and using
#the program turtle. While repeating 9 times.
import turtle
square = turtle.Turtle()
square.pensize(5)
square.shape("circle")
square.right(180)
square.forward(100)
square.left(90)
for aColor in ("red", "turquoise","blue", "green"):
    square.color(aColor)
    square.forward(100)
    square.left(90)
    square.forward(100)
    square.left(90)
    square.forward(300)
    square.left(90)
    
