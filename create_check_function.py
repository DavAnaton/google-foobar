def check_function(test_cases, expectations, sol_function):
	def check(index = None):
		toCheck = [index] if index!=None else [i for i, t in enumerate(test_cases)]
		for i in toCheck:
			ans = sol_function(test_cases[i])
			if ans == expectations[i]:
				print str(i) + " OK"
			else: 
				print str(i) + " ERROR"
				print "\texpected: " + str(expectations[i])
				print "\tgot:      " + str(ans)
	return check