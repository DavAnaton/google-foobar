import solution, sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
import create_check_function as create

test_cases = [
	[[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 0]],
	[[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]],
	[[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]],
]
expected = [
	6,
	7,
	11
]

create.check_function(test_cases, expected, solution.answer)()