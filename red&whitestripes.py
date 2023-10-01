#Name: Mohib Ahmed
#Date: Jun 8, 2023
#This program helps us create an image with stripes.
#Email: mohib.ahmed79@myhunter.cuny.edu

import numpy as np
import matplotlib.pyplot as plt

size = int(input("Enter size: "))
img = np.ones( (size,size,3) )
img[::2,:,1:] = 0
filename2 = input('Give the output variable please: ')
plt.imsave(filename2 , img)

