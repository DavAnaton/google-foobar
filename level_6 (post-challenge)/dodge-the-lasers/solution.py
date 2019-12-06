# Beatty sequence sum
# https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s

from decimal import Decimal, getcontext
getcontext().prec = 101
sqrt2 = Decimal(2).sqrt()

def solution(str_n):
	n = int(str_n)
	
	def nextSum(n):
		if(n == 0): return 0 
		if(n == 1): return 1 
		nPrime = long((sqrt2-1) * n)
		return n*nPrime + n * (n+1) / 2 - nPrime * (nPrime+1) / 2 - nextSum(nPrime)

	return str(nextSum(n))
