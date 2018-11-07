import solution, sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
import create_check_function as create

test_cases = [
	[1, 1],
	[3, 1, 7],
	[1, 7, 3, 21, 13, 19],
	[5, 5, 1, 1, 1, 1, 3, 3, 7, 7],
	[7, 7, 7, 9, 25, 1, 1],
	[5, 5, 5, 5, 1, 1, 1, 1],
	[10, 42, 6, 22],
]
expected = [
	2,
	1,
	0,
	2,
	3,
	0,
	0,
]

create.check_function(test_cases, expected, solution.answer)(6)