#Mohib Ahmed
#July 5th 2023
#Make a machine language program that adds 5 on itself
#Sample program that loops from 10 down to 0
ADDI $s0, $zero, 0 #set s0 to 0
ADDI $s1, $zero, 5  #use to decrement counter, $s0
AGAIN: ADD $s0, $s0, $s1
BEQ $s0, $zero, DONE
J AGAIN
Done:
