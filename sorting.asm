.data
array: .space 100
print: .asciiz "Enter The No Of Values in  The Array ::  "
print1: .asciiz "\n"
print2: .asciiz "\n Enter The Values \n "
print3: .asciiz "\n The Values in the array are \n"
print4 :.asciiz " "
.text
main:
li $v0,4
la $a0,print
syscall

li $v0,5
syscall
move $t1,$v0

li $t0,0
li $t2,0
li $t3,0
li $s1,0
li $v0,4
la $a0,print2
syscall

loop:
beq $t1,$t2,exit1
li $v0,5
syscall
sw $v0,array($t0)
addi $t0,$t0,4
addi $t2,$t2,1
j loop
exit1:
#sorting---
#-----
#-----
li $s0,0
li $s2,0
j loopsort
loopsort:
     addi $s0,$s0,1  
      li $s1,0
      li $s3,0
     bgt $s0,$t1,exitsort  
     j loop1sort
loop1sort:
     beq $s1,$t1,loopsortexit
     addi $s1,$s1,1
     lw $t4,array($s2)
     lw $t5,array($s3)
     blt $t4,$t5,swap
     addi $s3,$s3,4
     j loop1sort
swap:
sw $t4,array($s3)
sw $t5,array($s2)
addi $s3,$s3,4
j loop1sort
loopsortexit:
addi $s2,$s2,4
j loopsort
exitsort:
li $t3,0
li $s1,0
li $v0,4
la $a0,print3
syscall
loop1:
beq $t3,$t1,exit
lw $a0,array($s1)
li $v0,1
syscall
li $v0,4
la $a0,print4
syscall
addi $s1,$s1,4
addi $t3,$t3,1
j loop1
exit:
li $v0,10
syscall
