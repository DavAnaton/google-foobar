import solution, sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
import create_check_function as create

test_cases = [
	"wrw blf hvv ozhg mrtsg'h vkrhlwv?",
	"Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!",
]
expected = [
	"did you see last night's episode?",
	"Yeah! I can't believe Lance lost his job at the colony!!",
]

create.check_function(test_cases, expected, solution.answer)()