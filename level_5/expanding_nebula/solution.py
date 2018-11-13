import itertools
from copy import deepcopy
from collections import defaultdict
def answer(g):

	previous_states = [] # Keeps the unique last 2 lines of each possible previous states

	# Count how many times each an item from the array above can be obtained
	# Here, the default is 1 because the first line's ancestors can be obtained exactly once
	state_occurences = defaultdict(lambda:1)

	# Compute all previous possiblities to get True or False 
	possible_ancestors = [[[a[0], a[1]],[a[2], a[3]]] for a in itertools.product([True, False], repeat=	4)]
	possibilities_true = [ancestor for ancestor in possible_ancestors if sum(ancestor[0]) + sum(ancestor[1]) == 1]
	possibilities_false = [ancestor for ancestor in possible_ancestors if sum(ancestor[0]) + sum(ancestor[1]) != 1]

	# Transpose the graph to have a bidenmensionnal array where the lines are shorter than the columns
	h = len(g)
	w = len(g[0])
	if w > h:
		w, h = h, w
		g = map(list, zip(*g))

	'''
		Function that adds a cell's ancestors to the previous_states that are compatible
		@params ancestors, the list of ancestors for the next cell in the graph, as we go
		@returns None, the previous_states are modified directly
	'''
	def merge(ancestors):
		# For the first cell, there is no compatibility check
		if len(previous_states) == 0:
			previous_states[:] = ancestors
		else:
			new_previous_states = []
			for state in previous_states:
				for ancestor in ancestors:
					# How to merge ancestors for the first line of the graph:
					if len(state[0]) < w + 1:
						if state[0][-1] == ancestor[0][0] and state[1][-1] == ancestor[1][0]:
							new_previous_states.append([
								state[0] + [ancestor[0][1]],
								state[1] + [ancestor[1][1]]
							])
					# How to merge a new line's first cell's ancestors
					elif len(state[-1]) == w + 1:
						if state[-1][0] == ancestor[0][0] and state[-1][1] == ancestor[0][1]:
							new_line = state[:]
							new_line.append(ancestor[1])
							new_previous_states.append(new_line)
					# For the rest
					else:
						insert_index = len(state[-1])
						can_be_merged_bottom = (state[-2][insert_index - 1] == ancestor[0][0] and state[-2][insert_index] == ancestor[0][1])
						can_be_merged_left = (state[-1][insert_index - 1] == ancestor[1][0])
						if can_be_merged_left and can_be_merged_bottom:
							new_line = deepcopy(state)
							new_line[-1].append(ancestor[1][1])
							new_previous_states.append(new_line)
			# Update the global object
			previous_states[:] = new_previous_states

	"""
		Removes the first line of each element in previous_states,
		merges the similar second lines to only keep unique,
		and update the count of how many times each of these unique lines can be obtained
		@params state_occurences, the number of times each first line can be obtained
		@return new_state_occurences, the number of times each second line can be obtained
	"""
	def compress_first_line(state_occurences):
		# Default is 0 here because the second line can't be obtained alone
		# They depend on the first line's occurences
		new_state_occurences = defaultdict(lambda: 0)
		for state in previous_states:
			first_line = state.pop(0)
			remaining_line = state[0]
			new_state_occurences[str(remaining_line)] += state_occurences[str(first_line)]
		previous_states[:] = reduce(lambda l, x: l.append(x) or l if x not in l else l, previous_states, [])
		return new_state_occurences


	# Actual brute-forcing
	for index, line in enumerate(g):
		for cell in line:
			ancestors = (possibilities_true if cell else possibilities_false)[:]
			merge(ancestors)
		state_occurences = compress_first_line(state_occurences)

	return sum(state_occurences[str(a[0])] for a in previous_states)