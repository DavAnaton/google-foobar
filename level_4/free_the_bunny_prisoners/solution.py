import itertools
def answer(num_buns, num_required):
	bunny_map = [[] for i in range(0, num_buns)]
	# Each time you take (num_required - 1) bunnies that don't have a key K, all the rest of the bunnies have it.
	# This specific key K has to be distributed amongst num_buns - (num_required - 1) bunnies
	key_map = itertools.combinations(range(0, num_buns), num_buns - (num_required - 1))

	# Transpose the results
	for key, owning_bunnies in enumerate(key_map):
		for bunny in owning_bunnies:
			bunny_map[bunny].append(key)

	return bunny_map
