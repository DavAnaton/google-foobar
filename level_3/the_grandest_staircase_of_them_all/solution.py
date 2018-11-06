def answer(n):

	zeroArray = lambda  : [0] * (n+1);

	# We solve this problem by using dynamic programming.
	# We start solving the problem when we have 0 brick
	# then reccursively until n by keeping a memory of the previous steps.

	# Here the memory will be built like this:
	# - The line i describes the solutions when you have i bricks
	# - The column j describes the solutions when the last step has j bricks

	youHave0 = zeroArray()
	youHave0[0] = 1 # Finishing with 0 brick and using 0 is a valid move

	memory = [youHave0]
	for youHave in range(1, n+1):
		newLine = zeroArray()
		for youUse in range(1, youHave+1):
			solutionsAboveLastLevel = (x for nextStep, x in enumerate(memory[youHave - youUse]) if nextStep < youUse)
			newLine[youUse] = sum(list(solutionsAboveLastLevel))
		memory.append(newLine)	
	return sum(memory[n]) - 1 # Remove the case when we have just one step
