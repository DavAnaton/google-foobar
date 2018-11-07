import math
def answer(banana_list):
	is_pow_2 = lambda x : math.ceil(math.log(x, 2)) == math.floor(math.log(x, 2));
	can_cycle = lambda a, b: a != b not is_pow_2( a + b )
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

	# We assign the games randomly, for now
	for guard_1, can_be_paired_with in enumerate(can_cycle_map):
		for guard_2, can_be_paired in enumerate(can_be_paired_with):
			if can_be_paired and paired_with[guard_1] == None and paired_with[guard_2] == None:
				paired_with[guard_1] = guard_2
				paired_with[guard_2] = guard_1


	# If no guards can be paired or if the random anssignement found the best solution, no need for augmenting path
	if num_non_paired() <= 1 or num_paired() == 0:
		pass
	else:
		''' Look for augmenting path: 
			- starts and ends with a non-assigned guard with a non-assigned guard
			- contains only assigned guards
			Therefore, switching the directions of the assigned games in this path augments the number of assign guards
		'''
		starting_indexes = [i for i, v in enumerate(paired_with) if v == None]
		while starting_indexes:
			
			# Initializing BFS values
			queue = [starting_indexes.pop(0)]
			oldest_ancestor = -1
			parent = [None] * len(paired_with)
			parent[queue[0]] = oldest_ancestor
			found_ap = False

			if paired_with[queue[0]] != None:
				continue

			while queue:
				current_vertex = queue.pop(0)
				for neighbor, can_be_paired in enumerate(can_cycle_map[current_vertex]):
					if can_be_paired and parent[neighbor] == None:
						parent[neighbor] = current_vertex
						if paired_with[neighbor] == None:
							current_vertex = neighbor
							found_ap = True
							break;
						else:
							parent[paired_with[neighbor]] = neighbor
							queue.append(paired_with[neighbor])

				# Read augmenting path
				if found_ap:
					augmenting_path = []
					while current_vertex != -1:
						augmenting_path += [current_vertex]
						current_vertex = parent[current_vertex]
					break;
					
			if found_ap:
				# Swich assignements on the augmenting path
				for index in range(0, len(augmenting_path) - 1):
					if index % 2 == 0:
						paired_with[augmenting_path[index]] = augmenting_path[index + 1]
						paired_with[augmenting_path[index + 1]] = augmenting_path[index]

	return num_non_paired()

