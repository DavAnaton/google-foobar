import solution, sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
import create_check_function as create

test_cases = [
	(2, 1),
	(5, 3),
	(4, 4),
	(3, 2),
	(6, 0),
]
expected = [
	[[0], [0]],
	[[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9], [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]],
	[[0], [1], [2], [3]],
	[[0, 1], [0, 2], [1, 2]],
	[[], [], [], [], [], []],
]

solution_func = lambda params: solution.answer(*params)
create.check_function(test_cases, expected, solution_func)()