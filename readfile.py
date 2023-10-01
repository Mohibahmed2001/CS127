#Mohib Ahmed
#June 23 2023
#mohib.ahmed79@myhunter.cuny.edu
#We will read another csv files.

import pandas as pd

csv_file = input("Enter CSV file name: ")
data = pd.read_csv(csv_file)
top_factors = data['CONTRIBUTING FACTOR VEHICLE 1'].value_counts().head(3)
print("Top three contributing factors for collisions:")
print(top_factors)
