import copy;

def answer(mapped):
	maze = Maze(mapped)
	shortests_paths_from_begining = maze.runBFS(maze.beginning)
	shortests_paths_from_end = maze.runBFS(maze.end)
	indexes_of_walls = maze.getWallIndexes()
	return min([shortests_paths_from_begining[i]['cost'] + shortests_paths_from_end[i]['cost'] for i in indexes_of_walls]) + 1

class Maze():
	"""	Class that represents the maze as a list of indexes
		This class is used to find the shortest path after taking down one wall in a maze
		Its only constructor takes a bi-dimensional array of 0 and 1 (1 being a wall)
	"""
	def __init__(self, mapped):
		self.state = {'EMPTY':1, 'IN_QUEUE':2, 'VISITED':3}
		self.h = len(mapped)
		self.w = len(mapped[0])
		self.map = mapped

		self.beginning = 0
		self.end = self.h * self.w - 1

		# We set the graph as we need
		# each vertex is accessed by its index
		# no vertex has been visited yet, and the cost is infinity 
		self.mazeInfo = [{
			'i': index / self.w,
			'j': index % self.w, 
			'state': self.state['EMPTY'], 
			'cost': float('inf')
		} for index in range(0, self.h * self.w)]

		for cell in self.mazeInfo:
			cell['value'] = self.map[cell['i']][cell['j']]

	"""	Get the indexes of all the neighbours in the map of a given array
		@params: vertexIndex, the starting index
		@return: neighbours, an array of indexes
	"""
	def getNeighbours(self, vertexIndex):
		vertex = self.mazeInfo[vertexIndex]
		neighbours = []
		if vertex['i'] - 1 >= 0: # Up
			neighbours.append(vertexIndex - self.w)
		if vertex['i'] + 1 < self.h: # Down
			neighbours.append(vertexIndex + self.w)
		if vertex['j'] - 1 >= 0: # Left
			neighbours.append(vertexIndex - 1)
		if vertex['j'] + 1 < self.w: # Right
			neighbours.append(vertexIndex + 1)
		return neighbours
	
	""" Find the indexes of all the walls in the maze
		@return: an array of indexes
	"""
	def getWallIndexes(self):
		return [index for index, cell in enumerate(self.mazeInfo) if cell['value'] == 1]

	""" Find the shortests paths in the maze from a given index to the rest of the indexes
		@params: startingPoint, the index of the cell from where the BFS should start 
		@return: mappedMaze, an array of dict containing all the informations that we have after the BFS
							 Each dict has: the original coordinates of the cell (i and j)
											the state in which BFS left the cell (should be EMPTY or VISITED)
											the cost (distance) from starting point to this cell
	"""
	def runBFS(self, startingPoint):
		mappedMaze = copy.deepcopy(self.mazeInfo)

		#We initialize the BFS
		queue = [startingPoint]
		mappedMaze[startingPoint]['cost'] = 0

		# BFS iteration
		while queue:
			vertex = queue.pop(0)
			mappedMaze[vertex]['state'] = self.state['VISITED']
			neighbours = self.getNeighbours(vertex)
			for neighbour in neighbours:
				if mappedMaze[neighbour]['state'] == self.state['EMPTY']:
					mappedMaze[neighbour]['cost'] = mappedMaze[vertex]['cost'] + 1
					if mappedMaze[neighbour]['value'] == 0:
						queue.append(neighbour)
						mappedMaze[neighbour]['state'] = self.state['IN_QUEUE']
					else:
						mappedMaze[neighbour]['state'] = self.state['VISITED']
		return mappedMaze
