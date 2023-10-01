#Name: Mohib Ahmed
#Email: mohib.ahmed79@myhunter.cuny.edu
#Date: September 21, 2022
#This program asks for a string then prints out each letter with its
# ASCII and the letter two above it.
print("Enter a String: ", end="")
text = input()
textlength = len(text)
for char in text:
    ascii = ord(char)
    tom=chr(ord(char) + 2)
    print("letter", "\t", "ASCIII", "\t","next_two_letter")
    print(char, "\t", ascii, "\t", tom)
