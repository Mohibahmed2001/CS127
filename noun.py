#Name: Mohib Ahmed
#Date: Jun 13, 2023
#This program determines amount of nouns.
#Email: mohib.ahmed79@myhunter.cuny.edu
noun = input("Enter nouns: ")
words = noun.split()
amount = len(words)
print("Number of words: ", amount)
plural = noun.count('s ')

for i in noun:
    if i[-1] == "s":
        last = 1
    else:
        last = 0

plurals = plural + last
fraction = plurals / amount
print("Fraction of your list that is plural: ", fraction)
