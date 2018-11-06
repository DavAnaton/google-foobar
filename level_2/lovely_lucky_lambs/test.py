import solution, sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
import create_check_function as create

test_cases = [
	10,
	143,
]
expected = [
	1,
	3,
]

create.check_function(test_cases, expected, solution.answer)()