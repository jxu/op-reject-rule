# Translation of python code because why not

# $f4 = PI
# $f10, $f12, $f14 = arguments 1, 2, 3 (a, b, c)
# $a0 = argument 4 (level)
# $f20 = area (saved)


	.data	# CONSTANTS
PI:	.double	3.141592653589793
SAREA:	.double 2.1547005383792515	# 1 + 2/sqrt(3)
SRAD:	.double 2.030005838861446	# 3*pi*(1/start_rad)^2
NEGONE:	.double	-1.0

	.text
	.globl main
	
main:	l.d	$f4, PI		# Load floats
	l.d	$f20, SAREA
	
				# Repeat place_circle 3 times
	l.d	$f10, NEGONE	# Load pcirc arguments -1, SRAD, SRAD, 1
	l.d	$f12, SRAD
	l.d	$f14, SRAD
	li	$a0, 1
	
	jal	pcirc

	li	$v0, 10		# Exit
	syscall
	
pcirc:	addi	$sp, $sp, -28	# Push $ra, $a0, $f10, $f12, $f14
	sw	$ra, 0($sp)	
	sw	$a0, 4($sp)
	s.d	$f10, 8($sp)
	s.d	$f12, 16($sp)
	s.d	$f14, 24($sp)
	
	jr	$ra		# Return to main
