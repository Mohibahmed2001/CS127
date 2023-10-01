#Name:  Mohib Ahmed
#Date:  10/25/2022
#Email: mohib.ahmed79@myhunter.cuny.edu
#using pandas to sort data
import pandas as pd
df = pd.read_csv('children_lead.csv')
print(df)
choice = input("a. group by borough \nb. group by year\n")
if choice == 'a':
    print("\nexpected average number of affected children grouped by borough")
    print("Bronx",df[df["borough"] == 'Bronx']['affected_children'].mean())
    print("Brooklyn",df[df["borough"] == 'Brooklyn']['affected_children'].mean())
    print("Manhattan",df[df["borough"] == 'Manhattan']['affected_children'].mean())
    print("Queens",df[df["borough"] == 'Queens']['affected_children'].mean())
    print("Staten Island",df[df["borough"] == 'Staten Island']['affected_children'].mean())
    value = input("User please give me the borough:")
    print("\n\nexpeceted average, min and max of ", value)
    print("Average number of affected children of",value ,"is",df[df["borough"] == value]['affected_children'].mean())
    print("min number of affected children of",value ,"is",df[df["borough"] == value]['affected_children'].min())
    print("max number of affected children of",value ,"is",df[df["borough"] == value]['affected_children'].max())
else:
    print("2005",df[df["year"] == 2005]['affected_children'].mean())
    print("2006",df[df["year"] == 2006]['affected_children'].mean())
    print("2007",df[df["year"] == 2007]['affected_children'].mean())
    print("2008",df[df["year"] == 2008]['affected_children'].mean())
    print("2009",df[df["year"] == 2009]['affected_children'].mean())
    print("2010",df[df["year"] == 2010]['affected_children'].mean())
    print("2011",df[df["year"] == 2011]['affected_children'].mean())
    print("2012",df[df["year"] == 2012]['affected_children'].mean())
    print("2013",df[df["year"] == 2013]['affected_children'].mean())
    print("2014",df[df["year"] == 2014]['affected_children'].mean())
    print("2015",df[df["year"] == 2015]['affected_children'].mean())
    print("2016",[df["year"] == 2016]['affected_children'].mean())
    
                  



