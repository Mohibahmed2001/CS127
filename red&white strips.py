#Name: Mohib Ahmed
#Date: May 30, 2001
#This program makes blues
#Email: mohib.ahmed79@myhunter.cuny.edu

import matplotlib.pyplot as plt
import numpy as np
filename = input('Enter name of the input file:  ')
img = plt.imread(filename)
plt.imshow(img)
plt.show()
img2 = img.copy()
img2[:,:,1] = 0
img2[:,:,0] = 0
plt.imshow(img2)
plt.show()
filename2 = input('Give the output variable please: ')
plt.imsave(filename2 , img2)
