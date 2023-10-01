#Name: Mohib Ahmed
#Email: mohib.ahmed79@myhunter.cuny.edu
#Date: September 21, 2022
#This program asks for a string then shifts it as many letters as the
# user requets.
plain = input("What is your plaintext? ")
shif = int(input("What is your shift? "))

def caesar(plain, shif): 
  cipherText = ""
  for ch in plain:
    if ch.isalpha():
      stayt = ord(ch) + shif 
      if stayt > ord('z'):
        stayt -= 26
      finalLetter = chr(stayt)
      cipherText += finalLetter
  print ("Your cipher is ", cipherText)
  return cipherText
caesar(plain, shif)
