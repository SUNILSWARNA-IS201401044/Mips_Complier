.data
.txt

main:
	add $t1,$t2,$t3
	add $t4,$t1,$t2
	lw $t5,8($t4)
	add $t7,$t6,$t5
	add $t8,$t1,$t5
	beq $t8,$t9,Else
	Else:
		add $t9,$t4,$t0
		add $t10,$t6,$t9
		add $t11,$t10,$t9
