# Translation of python code because why not

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
	
					# Repeat place_circle 3 times
	l.d	$f10, ONE		# Load pcirc arguments -1, SRAD, SRAD, 1
	neg.d	$f10, $f10		# a = -1
	l.d	$f12, SRAD
	l.d	$f14, SRAD
	li	$a0, 1
	
	jal	pcirc

	li	$v0, 10			# Exit
	syscall
	
pcirc:	addi	$sp, $sp, -28		# Push $ra, $a0, $f10, $f12, $f14
	sw	$ra, 0($sp)		
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
	
	div.d	$f16, $f22, $f16	# temp = 1/d
	mul.d	$f16, $f16, $f16	# temp = temp*temp
	mul.d	$f16, $f16, $f24	# temp *= PI  
	add.d	$f20, $f20, $f16	# area += temp  (pi*(1/d)^2)

	
	jr	$ra			# Return to main
