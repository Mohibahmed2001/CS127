#Name: Mohib Ahmed
#Date: May 30, 2023
#This program helps us learn lens indepth and range feature.
#Email: mohib.ahmed79@myhunter.cuny.edu
newmsg = ''
message = input('Please give me your mssg nerd: ')
ls = len(message)
for i in range(0,ls-1):
    print (message[0:i])
for i in range(0,ls-1):
    print(message[i:ls])
    
