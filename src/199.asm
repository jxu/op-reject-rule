# Translation of python code for the challenge 
# Completed program (10 levels) takes forever to run in MARS but runs in SPIM!
# To-do: Print rounded

# $f10, $f12, $f14 = arguments 1, 2, 3 (a, b, c)
# $a0 = argument 4 (level)
# $f20 = area (saved)
# $f22, $f24 = ONE, PI


	.data	# CONSTANTS
PI:	.double	3.141592653589793
SRAD:	.double 2.1547005383792515	# 1 + 2/sqrt(3)
SAREA:	.double 2.030005838861446	# 3*pi*(1/start_rad)^2
ONE:	.double	1.0

	.text
	.globl main
	
main:	l.d	$f22, ONE		# Load floats
	l.d	$f24, PI
	l.d	$f20, SAREA		
	
	li	$t0, 3			# Repeat place_circle 3 times
ml:	l.d	$f10, ONE		# Load pcirc arguments (-1, SRAD, SRAD, 1)
	neg.d	$f10, $f10		# a = -1
	l.d	$f12, SRAD
	l.d	$f14, SRAD
	li	$a0, 1
	jal	pcirc
	
	sub	$t0, $t0, 1
	bgtz	$t0, ml
	
	l.d	$f10, SRAD		# Load pcirc arguments (SRAD, SRAD, SRAD, 1)
	l.d	$f12, SRAD
	l.d	$f14, SRAD
	li	$a0, 1
	jal 	pcirc
	
	sub.d	$f20, $f24, $f20	# ratio = PI - area
	div.d	$f20, $f20, $f24	# ratio /= PI
	
	li	$v0, 3			# Print ratio
	mov.d	$f12, $f20
	syscall

	li	$v0, 10			# Exit
	syscall
	
	
pcirc:	addi	$sp, $sp, -36		# Push $ra, $a0, $f10, $f12, $f14, leave room for d (40 bytes)
	sw	$ra, 0($sp)		# |$ra |$a0 |$f10     |$f12     |$f14     |d        |
	sw	$a0, 4($sp)		
	s.d	$f10, 8($sp)
	s.d	$f12, 16($sp)
	s.d	$f14, 24($sp)
	
	mul.d	$f16, $f10, $f12	# d = a*b
	mul.d	$f18, $f10, $f14	# temp = a*c
	add.d	$f16, $f16, $f18	# d += temp
	mul.d	$f18, $f12, $f14	# temp = b*c
	add.d	$f16, $f16, $f18	# d += temp  (d = a*b + a*c + b*c)
	sqrt.d	$f16, $f16		# d = sqrt(d)
	add.d	$f16, $f16, $f16	# d *= 2
	add.d	$f16, $f16, $f10	# d += a
	add.d	$f16, $f16, $f12	# d += b
	add.d	$f16, $f16, $f14	# d += c  (d = 2*sqrt(a*b + a*c + b*c) + a + b + c)
	s.d	$f16, 32($sp)		# Store d
	
	div.d	$f18, $f22, $f16	# temp = 1/d
	mul.d	$f18, $f18, $f18	# temp = temp*temp
	mul.d	$f18, $f18, $f24	# temp *= PI  
	add.d	$f20, $f20, $f18	# area += temp  (temp = pi*(1/d)^2)
	
	beq	$a0, 10, pcexit		# Exit loop if level == MAX_LEVEL
	
pcl:	#l.d	$f10, 8($sp)		# Load arguments from stack (a, b, d, level+1)
	#l.d	$f12, 16($sp)		# (a and b should be same from parameters)
	mov.d	$f14, $f16
	#lw	$a0, 4($sp)
	add	$a0, $a0, 1
	add	$sp, $sp, -4		# *Force doubleword align???
	jal	pcirc		
	add	$sp, $sp, 4		# *Mystery alignment 
	
	l.d	$f10, 8($sp)		# Load arguments (a, c, d, level+1)
	l.d	$f12, 24($sp)		
	l.d	$f14, 32($sp)
	lw	$a0, 4($sp)
	add	$a0, $a0, 1
	add	$sp, $sp, -4		# *
	jal	pcirc		
	add	$sp, $sp, 4		# *
	
	l.d	$f10, 16($sp)		# Load arguments (b, c, d, level+1)
	l.d	$f12, 24($sp)		
	l.d	$f14, 32($sp)
	lw	$a0, 4($sp)
	add	$a0, $a0, 1
	add	$sp, $sp, -4		# *
	jal	pcirc		
	add	$sp, $sp, 4		# *
	

pcexit:	lw	$ra, 0($sp)		# Restore $ra
	addi	$sp, $sp, 36		# Restore $sp
	jr	$ra			# Return 
