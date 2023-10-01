#Mohib Ahmed
#June 23,2023
#mohib.ahmed79@myhunter.cuny.edu
#We will read a parking ticket file.

import pandas as pd
#filename=input("please type in the parking ticket file name")
#attribute = input("Please give me the attribute to check")
#print("The 10 worst offenders are:")
#print(filename[attribute].value_counts()[:10]) #Print out the dataframe

csvFile = input('Enter CSV file name: ')         #Name of the CSV file
tickets = pd.read_csv(csvFile)     #Read in the file to a dataframe
attribute = input("Please give me the attribute to check")
print("The 10 worst offenders are:")
print(tickets[attribute].value_counts()[:10]) #Print out the dataframe
