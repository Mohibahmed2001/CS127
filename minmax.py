#Name: Mohib Ahmed
#Date: Jun 16, 2023
#This program helps us use max and avg.
#Email: mohib.ahmed79@myhunter.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5)
borough = input("Please give me borogh")
print("The largest number living in the ",borough, "is", pop[borough].max())
print("The average number living in the ",borough, "is", pop[borough].mean())
