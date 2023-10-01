#Name: Mohib Ahmed
#Date: May 30, 2001
#Email: mohib.ahmed79@myhunter.cuny.edu
#This program makes a code
code = input("Please give me your code: ")
coder = ""
for i  in code:
    offset = ord(i)-ord('a')+13
    wrap = offset%26
    new =(chr(ord('a')+wrap))
    coder = coder + new
print("Your word in code is: ")
print(coder)
