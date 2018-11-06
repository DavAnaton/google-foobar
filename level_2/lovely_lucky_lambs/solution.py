import math
def answer(total_lambs):
	if(total_lambs <= 2):
		return 0
	""" Generous case, with less henchmen
	    The payroll will look like the following [2^0, 2^1, ..., 2^biggest_power, remaining]
	    The sum of this array minus the last term is 2^(biggest_power + 1) - 1"""
	biggest_power = int(math.floor(math.log(total_lambs + 1, 2)) - 1)
	generous_case = biggest_power + 1 # All the powers + 2^0
	remaining_lambs_for_last_henchman = total_lambs - (2 ** (biggest_power + 1) - 1)
	if(remaining_lambs_for_last_henchman >= 2**biggest_power + 2**(biggest_power - 1) ):
		generous_case += 1

	""" Stingy cass, with more henchmen
	    The payroll will look like the following [f_0, ..., f_n] where f_n is the nth number of the fibonnacci sequence
	    The sum of this array is f_(n+2) - 1 which must be inferior to total_lambs"""

	# Mathematical formulas for fibonacci
	phi = (1+5**0.5)/2
	phi_prime = (1 - (5**0.5))/2
	compute_fibonacci = lambda n : int((phi**n - phi_prime**n)/(5**0.5))
	find_fibonacci_index = lambda value : int(round(math.log(value * 5**0.5) / math.log(phi)))

	# Computation of stingy case
	fn2 = total_lambs + 1 # f_(n+2) - 1 = total_lambs
	closest_index = find_fibonacci_index(fn2)
	closest_fibonacci = compute_fibonacci(closest_index)
	if(closest_fibonacci > fn2):
		closest_index -= 1
	stingy_case = closest_index - 2 # closest_index contains n + 2

	return stingy_case - generous_case