#Name: Mohib Ahmed
#Email: mohib.ahmed79@myhunter.cuny.edu
#Date: September 21, 2022
#This program asks for a string then prints out each letter with its
# ASCII and the letter two above it.
print("Enter a String: ", end="")
text = input()
textlength = len(text)
print("%6s %6s %15s"%("letter", "ASCIII","next_two_letter"))
for character in text:
    ASCII_code_of_character = ord(character)
    next_two_letter_of_character=chr(ord(character) + 2)
    print("%6c %5i %15c"%(character, ASCII_code_of_character, next_two_letter_of_character))
   

