.data
 str: .asciiz "Enter a lower string: "
 str1: .asciiz "The upper case string : "
 buffer: .space 30
 
 
main:
.text
	
	li $t9, 5
	li $t8, 0
	
	la $a0, str
	li $v0, 4
	syscall
	
	li $a1, 30
	la $a0, buffer
	li $v0, 8
	syscall
	
	la $t0, buffer
	
	l1:   
		lb $t1, 0($t0)
		beqz $t1, exit
		beq $t1, 10, exit
		addiu $t1, $t1, -32 
		sb $t1, 0($t0)	
		 
		addiu $t0,$t0,1 
		j l1

	  
	exit:
	li $v0,4
	la $a0,str1
	syscall
		li $v0, 4
	
		la $a0, buffer
		syscall
		
		li $v0, 10
		syscall
