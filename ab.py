value = input("Please give ur string\n")
words = value.split()
value = value + " "
for i in range(len(value)):
         # If current character is a space
        if value[i] == ' ':
            # Then previous character must be
            # the last character of some word
            if value[i - 1]== "a" or value[i - 1]== "b" :
                slam = print(value[i-1],end = "")

x = len(slam)
y = len(words)
print("number of words with a or b:",x)
print("number of words:",y)

