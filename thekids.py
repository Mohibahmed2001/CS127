#Name: Mohib Ahmed
#Date: Jun 20, 2023
#This program asks for names and oragnizes them.
#Email: mohib.ahmed79@myhunter.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd
inputfile = input("Please give ipnput file names:")
pop = pd.read_csv(inputfile,skiprows=0)
pop['Fraction'] = pop['Total Children in Shelter']/pop['Total Individuals in Shelter']
pop.plot(x = "Date of Census", y = "Fraction")
fig = plt.gcf()
outputfile = input('Give the output variable please: ')
fig.savefig(outputfile)
