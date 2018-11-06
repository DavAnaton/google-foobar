import solution, sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
import create_check_function as create

test_cases = [
	3,
	200,
]
expected = [
	1,
	487067745,
]

create.check_function(test_cases, expected, solution.answer)()