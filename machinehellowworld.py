#Mohib Ahmed
#July 5 2023
#Using a machine language program that prints hello world
ADDI $sp, $sp, -13
ADDI $t0, $zero, 72 #ASCII NUMS
SB $t0, 0($sp)
ADDI $t0, $zero, 101 
SB $t0, 1($sp)
ADDI $t0, $zero, 108 
SB $t0, 2($sp)
ADDI $t0, $zero, 108
SB $t0, 3($sp)
ADDI $t0, $zero, 111 
SB $t0, 4($sp)
ADDI $t0, $zero, 44
SB $t0, 5($sp)
ADDI $t0, $zero, 32 
SB $t0, 6($sp)
ADDI $t0, $zero, 119 
SB $t0, 7($sp)
ADDI $t0, $zero, 87 
SB $t0, 8($sp)
ADDI $t0, $zero, 114 
SB $t0, 9($sp)
ADDI $t0, $zero, 108 
SB $t0, 10($sp)
ADDI $t0, $zero, 100 
SB $t0, 11($sp)
ADDI $t0, $zero, 33 
SB $t0, 12($sp)
ADDI $t0, $zero, 0 
SB $t0, 13($sp)

ADDI $v0, $zero, 4 # 4 is for print string
ADDI $a0, $sp, 0
syscall 		
