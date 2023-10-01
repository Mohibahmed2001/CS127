#Name: Mohib Ahmed
#Date: May 30, 2001
#This program makes blues
#Email: mohib.ahmed79@myhunter.cuny.edu

import turtle				

turtle.colormode(255)		
syeda = turtle.Turtle()		
syeda.shape("turtle")		
syeda.backward(100)			

for i in range(0,255,10):
     syeda.forward(10)		
     syeda.pensize(i)	     
     syeda.color(0,0,i)	

