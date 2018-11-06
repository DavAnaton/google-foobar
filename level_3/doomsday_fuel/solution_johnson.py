from fractions import Fraction
from collections import defaultdict
from copy import deepcopy
def answer(matrix):
	n = len(matrix)
	norms = normalization(matrix)
	all_cycles = johnson(matrix)

	# BFS traversal of the graph to update the costs
	costs = [0 for vertex in matrix]
	queue = [0]
	costs[0] = 1
	STATUSES = {"EMPTY": 0, "VISITED": 1}
	status = [0 for vertex in matrix]

	while queue:
		vertex = queue.pop(0)
		for cycle in all_cycles:
			if vertex in cycle:
				all_cycles.remove(cycle)
				costs[vertex] *= weight_of_cycled_path(matrix, cycle)
		for neighbour, edge in enumerate(matrix[vertex]):
			if edge and status[neighbour] == STATUSES["EMPTY"]:
				costs[neighbour] += costs[vertex] * edge
				queue += [neighbour]
		status[vertex] = STATUSES["VISITED"]

	#Formatting of the results
	result = []
	denominator = max([c.denominator for c in costs])
	for vertex, cost in enumerate(costs):
		if norms[vertex] == 0:
			result.append(cost.numerator * denominator / cost.denominator)
	result.append(denominator)
	return result

""" Normalizes the passed in graph
	changes the graph passed in as a first parameter so the sum of each line will be 1
	@params: graph, a bidimensional distance matrix
	@returns: norms, an array containing the previous norm of each line
"""
def normalization(graph):
	norms = []
	for i, line in enumerate(graph):
		norms.append(sum(line))
		if norms[i] != 0:
			for j, vertex in enumerate(line):
				graph[i][j] = Fraction(graph[i][j], norms[i])
	return norms	

""" Compute the weight a given cycle in a given graph
	**CAUTION**: this function works only for a probality graph
	@params: graph, the bidimensional distance matrix
			 cycle, the array containing all the vertex indexes
	@return: weight, the sum of the weights of all the paths looping in this cycle
"""
def weight_of_cycled_path(graph, cycle):
	weight_of_cycle = 1
	for index, vertex in enumerate(cycle):
		weight_of_cycle *= graph[vertex][cycle[(index + 1)%len(cycle)]]
	# weight_of_cycle is the weight of 1 loop
	# The weight of all number of loop is given by the formula:
	# Sum[0->infinity](weight_of_cycle ^ n) = 1 / (1 - weight_of_cycle)
	return 1 / (1 - weight_of_cycle)


""" Johnson's algorithm to find all the simple cycles in a given graph
	@params: graph, a bidimensional distance matrix
	@return: cycles, the list of cylces sorted by length
"""
def johnson(graph):
	cycles = []

	stack = []
	block_set = []
	block_map = defaultdict(lambda: [])
	graph = deepcopy(graph)

	def johnson_explore(index):
		stack.append(index)
		block_set.append(index)
		neighbours = [e for e, v in enumerate(graph[index]) if v > 0 and e in current_component]
		found_cycle = False
		for neighbour in neighbours:
			if neighbour == start_index:
				found_cycle = True
				cycles.append(deepcopy(stack))
			elif not neighbour in block_set:
				found_cycle |= johnson_explore(neighbour)
		stack.pop()
		if found_cycle:
			unblock(index)
		else:
			for neighbour in neighbours:
				block_map[neighbour].append(index)
		return found_cycle

	def unblock(index):
		if index in block_set:
			block_set.pop(block_set.index(index))
		if block_map[index]:
			for vertex in block_map[index]:
				unblock(vertex)
			del block_map[index]

	def remove_vertex(index):
		for i in range(0, len(graph)):
			for j in range(0, len(graph)):
				if i == index or j == index:
					graph[i][j] = 0


	scc = [component for component in kosaraju(graph) if (len(component) > 1)]
	while len(scc) > 0:
		current_component = scc[0]
		start_index = current_component[0]
		johnson_explore(start_index)
		remove_vertex(start_index)
		scc = [component for component in kosaraju(graph) if (len(component) > 1)]

	return sorted(cycles, key=len)

""" Kosaraju's Algorithm
	Finds strongly connected components
	@params: graph
	@returns: components, an array of arrays; each array contains the vertex in the SCC
"""
def kosaraju(graph):
	stack = dfs(graph, 0)
	transpose = [[] for i in range(0, len(graph))]
	for i in range(0, len(graph)):
		for j in range(0, len(graph)):
			transpose[j].append(graph[i][j])
	in_component = [False for vertex in graph]
	components = []
	while stack:
		vertex = stack.pop()
		if not in_component[vertex]:
			component = dfs(transpose, vertex, in_component)
			for new_vertex in component:
				in_component[new_vertex] = 1
			components.append(component)
	return components

""" Run DFS on given graph
	@params: graph, the graph as a bidimensional distance matrix
			 start, the index of the starting vertex
			 block_DFS, an array where each index indicates if the corresponding vertex should stop the DFS,
			 			True, if we only want a DFS tree
						If block DFS is not given, we will run until all the vertices are explored
	@return: finish_times, the vertex ordered according to their finish_times
"""
def dfs(graph, start, block_DFS=None):
	STATE = {"EMPTY": 0, "PROCESSING": 1, "VISITED": 2}
	states = [STATE["EMPTY"] for vertex in graph]
	finish_times = []

	""" DFS iteration
		visits children of the given index then mark it as visited
		@params: index
	"""
	def dfs_iter(index):
		states[index] = STATE["PROCESSING"]
		for v, e in enumerate(graph[index]):
			if e > 0 and states[v] == STATE["EMPTY"]:
				if not (block_DFS and block_DFS[v]):
					dfs_iter(v)
		finish_times.append(index)
		states[index] = STATE["VISITED"]

	dfs_iter(start)
	if not block_DFS:
		try:
			non_visited = states.index(STATE["EMPTY"])
		except:
			pass
		else:
			dfs_iter(non_visited)
	return finish_times

def display(mat):
	n = len(mat)
	representation = "\n"
	for i in range(0, n):
		for j in range(0, n):
			representation += str(mat[i][j]) + " "
		representation += "\n"
	print representation
