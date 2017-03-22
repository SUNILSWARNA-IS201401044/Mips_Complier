.data
msg1: .asciiz "Enter Multiplicand: "
msg2: .asciiz "Enter Multiplier: "
msg3: .asciiz "The product is: "
.text
.globl main
main:
	li $v0,4
	la $a0,msg1
	syscall
	
	li $v0,5
	syscall
	move $s0,$v0
	
	li $v0,4
	la $a0,msg2
	syscall
	
	li $v0,5
	syscall
	move $s1,$v0
	
mult:
	li $s3,0
	li $t1,1
	li $t2,0
	loop:
		beq $s1,$0,done
		
		and $t2,$t1,$s1 #getting lsb of multiplier
		beq $t2,1,loop_add
		beq $t2,0,loop_shift
		
		loop_add:
			addu $s3,$s3,$s0
		loop_shift:
			sll $s0,$s0,1
			srl $s1,$s1,1
			j loop
done:
	li $v0,4
	la $a0,msg3
	syscall
			
	li $v0,1
	move $a0,$s3
	syscall
			
	li $v0, 10
	syscall
					
