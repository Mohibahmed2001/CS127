#MOHIB AHMED
#June 30,2001
#mohib.ahmed79@myhunter.cuny.edu
#Make a random turtle

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(10)
  a = random.randrange(360)#We only change this line and just remove the third num
  trey.right(a)
