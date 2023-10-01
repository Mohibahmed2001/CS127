#Name: Mohib Ahmed
#Date: Jun 13, 2023
#This program determines the snow total.
#Email: mohib.ahmed79@myhunter.cuny.edu

import numpy as np
import matplotlib.pyplot as plt
snowpic = input("please input the pictures name")
snow = plt.imread(snowpic)
countSnow = 0            
t = 0.75    #range for white             
for i in range(snow.shape[0]):
     for j in range(snow.shape[1]):
          if (snow[i,j,0] > t) and (snow[i,j,1] > t) and (snow[i,j,2] > t):
               countSnow = countSnow + 1

print("Snow count is", countSnow)
