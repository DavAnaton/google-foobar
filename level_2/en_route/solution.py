def answer(hallway):
	hellos = 0
	walkingRight = 0
	for char in hallway:
		if char == '>':
			walkingRight+=1
		elif char == '<':
			hellos += walkingRight * 2
	return hellos