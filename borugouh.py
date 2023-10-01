#Name: Mohib Ahmed
#Date: Jun 16, 2023
#This program creates a borough graph.
#Email: mohib.ahmed79@myhunter.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5)
borough = input("Please give me borogh")
pop['Fraction'] = pop[borough]/pop['Total']
pop.plot(x = 'Year', y = 'Fraction')
fig = plt.gcf()
outputfile = input('Give the output variable please: ')
fig.savefig(outputfile)
