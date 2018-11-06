import fractions
from copy import deepcopy
import math

def answer(graph):
	matrix = Matrix(graph)
	norms = matrix.normalization()

	# If s0 is stable
	if norms[0] == 0:
		result = [0 for i in graph]
		result[0] = 1
		result.append(1)
		return result

	#########################
	# Absorbing Markov chains
	#########################
	# Decomposition of the graph like so 
	# G = | Q  R |
	#     | 0  I |
	# Q being a square matrix which size is the size of all the non-absorbing lines
	# I is the identity
	# R is the remaining matrix
	absorbing_states = [index for index, value in enumerate(norms) if value == 0]
	non_absorbing_lines = [line for i, line in enumerate(matrix) if i not in absorbing_states]
	q, r = [], []
	for line in non_absorbing_lines:
		q.append([value for i, value in enumerate(line) if i not in absorbing_states])
		r.append([value for i, value in enumerate(line) if i in absorbing_states])
	Q = Matrix(q)
	R = Matrix(r)

	# Now that the decomposition is done, we compute the probability of each non-absorbing compononent to 
	# decompose in each absorbing component using the formula 
	# P = (I - Q)^-1 * R
	# We take the first line because we start with s0 only
	probabilities = ((Matrix.identity(len(Q)) - Q) ** -1 * R)[0]

	#########################
	# Formatting the results
	#########################
	# The denominator will be the LCM of all denominators
	denominator = 1
	for f in probabilities:
		denominator *= f.denominator / fractions.gcd(denominator, f.denominator)
	result = [f.numerator * denominator / f.denominator for f in probabilities]
	result.append(denominator)

	return result


class Matrix(object):
	def __init__(self, values):
		if isinstance(values, Matrix):
			self._values = deepcopy(values._values)
			self._h = values._h
			self._w = values._w
		else:
			self._values = values
			self._h = len(values)
			self._w = len(values[0])

	def __add__(self, mat):
		if(self._w != mat._w or self._h != mat._h):
			raise ValueError("Addition of 2 matrix not possible")
		else:
			new_mat = Matrix(mat)
			for i in range(0, self._h):
				for j in range(0, self._w):
					new_mat[i][j] += self._values[i][j]
			return new_mat

	def __neg__(self):
		new_mat = Matrix(self)
		for i in range(0, self._h):
			for j in range(0, self._w):
				new_mat[i][j] = -self._values[i][j]
		return new_mat

	def __sub__(self, mat):
		if(self._w != mat._w or self._h != mat._h):
			raise ValueError("Substraction of 2 matrix not possible")
		else:
			return self + (-mat)

	def __mul__(self, mat):
		if(self._w != mat._h):
			raise ValueError("Multiplication of 2 matrix not possible")
		else:
			new_mat = []
			for i in range(0, self._h):
				new_mat.append([])
				for j in range(0, mat._w):
					new_mat[i].append(0)
					for k in range(0, self._w):
						new_mat[i][j] += self[i][k] * mat[k][j]
			return Matrix(new_mat)

	def __pow__(self, pow):
		try:
			n = len(self)
		except Exception as e:
			raise ValueError("Cannot compute " + ("power" if pow!=-1 else "inverse") + " of non-square matrix")
		mat = Matrix(self)
		if pow == 0:
			for i in range(0, n):
				for j in range(0, n):
					mat[i][j] = 1 if i==j else 0
		elif pow == -1:
			det = self.determinant()
			if n == 1:
				mat = Matrix([[1/det]])
			else:
				for i in range(0, n):
					for j in range(0, n):
						mat[i][j] = int(((i+j+1) % 2 - 0.5) * 2) * Matrix._det(Matrix._submatrix(self, i, j))/det
				mat = mat.transpose()
		elif pow > 0:
			for i in range(1, pow):
				mat *= self
		else:
			return (mat**-1)**(pow*-1)
		return mat

	def __len__(self):
		if(self._w == self._h):
			return self._w
		elif self._w == 1:
			return self._h
		else:
			raise ValueError("Cannot calculate length of non-square matrix")

	def __getitem__(self, i):
		return self._values[i]

	def __repr__(self):
		representation = ""
		for i in range(0, self._h):
			for j in range(0, self._w):
				representation += str(self._values[i][j]) + " "
			representation += "\n"
		return representation

	""" Create identity matrix of given size
		@params: size, the dimension of the require identity
		@return: mat, a size*size matrix that contains 1 on the main diagonal, 0 elsewhere
	"""
	@staticmethod
	def identity(size):
		mat = []
		for i in range(0, size):
			mat.append([])
			for j in range(0, size):
				mat[i].append(int(i == j))
		return Matrix(mat)

	""" Compute the determinant of a given matrix
		@params: mat, a matrix
		@return: det, its determinant
	"""
	@staticmethod
	def _det(mat):
		try:
			# TODO: fix for vectors
			n = len(mat)
		except Exception as e:
			raise ValueError("Cannot compute determinant of non-square matrix")
		if n == 1:
			return mat[0][0] if isinstance(mat[0], list) else mat[0]
		det = 0
		for i in range(0, n):
			submatrix = Matrix._submatrix(mat, 0, i)
			det += (-1)**(i%2) * mat[0][i] * Matrix._det(submatrix)
		return det

	""" Compute the submatrix if we exclude the ith line and jth column
		@params: mat, a matrix
				 i, index of the line to remove
				 j, index of the column to remove
				 do_not_copy, a boolean that says if we need to work on a copy or the original (False by default)
		@return: submatrix, a matrix with the removed line and column
	"""
	@staticmethod
	def _submatrix(mat, i, j, do_not_copy = False):
		values = mat._values if isinstance(mat, Matrix) else mat
		submatrix = deepcopy(values)
		submatrix.pop(i)
		for k in range(0, len(mat) - 1):
			submatrix[k].pop(j)
		return submatrix

	""" Normalizes the graph
		changes the current instance so the sum of each line will be 1
		@returns: norms, an array containing the previous norm of each line
	"""
	def normalization(self):
		norms = []
		for i, line in enumerate(self._values):
			norms.append(sum(line))
			if norms[i] != 0:
				for j, vertex in enumerate(line):
					self._values[i][j] = fractions.Fraction(self._values[i][j], norms[i])
		return norms

	""" Compute the determinant of the current instance
		@return: det, its determinant
	"""
	def determinant(self):
		return Matrix._det(self)

	""" Compute the trace of the current instance
		@return: trace, its trace
	"""
	def trace(self):
		try:
			n = len(self)
		except Exception as e:
			raise ValueError("Cannot compute trace of non-square matrix")
		trace = 0
		for i in range(0, n):
			trace += self[i][i]
		return trace

	""" Transpose the current instance """
	def transpose(self):
		t = []
		for i in range(0, self._w):
			t.append([])
			for j in range(0, self._h):
				t[i].append(self[j][i])
		return Matrix(t)
