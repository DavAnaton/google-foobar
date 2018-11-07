import math
def answer(banana_list):
	is_pow_2 = lambda x : math.ceil(math.log(x, 2)) == math.floor(math.log(x, 2));
	can_cycle = lambda a, b: a != b and not is_pow_2( a + b )
	paired_with = [None] * len(banana_list)
	num_non_paired = lambda: paired_with.count(None)
	num_paired = lambda: len(paired_with) - num_non_paired()

	# Turn banana_list into a graph:
	# We add an edge between two guards only if they can play together and stay in a loop
	can_cycle_map = []
	for guard_1, banana_1 in enumerate(banana_list):
		can_cycle_map.append([
			can_cycle(banana_1, banana_2) if guard_1 != guard_2 
			else False 
			for guard_2, banana_2 in enumerate(banana_list)
		])

	guards = range(0, len(banana_list))
	guards.sort(key = lambda index:len([pairing for pairing in can_cycle_map[index] if pairing]))

	for first_guard in guards:
		for second_guard in guards:
			if can_cycle_map[first_guard][second_guard] and paired_with[first_guard] == None and paired_with[second_guard] == None:
				paired_with[first_guard] = second_guard
				paired_with[second_guard] = first_guard
							
	return num_non_paired()
