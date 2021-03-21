# encoding: utf-8
INITIALIZE_DIFFICULTY_LEVEL = 'initialize.difficulty'
INCREASE_DIFFICULTY_LEVEL = 'increase.difficulty'
DECREASE_DIFFICULTY_LEVEL = 'decrease.difficulty'

DIFFICULTY_OPERAND_MAP = {
	"easy1": {"operand1": [1,1], "operand2":[1, 10]},
	"easy2": {"operand1": [2,5], "operand2":[2, 5]},
	"medium1": {"operand1": [2,5], "operand2":[6, 10]},
	"medium2": {"operand1": [6,12], "operand2":[2, 5]},
	"hard": {"operand1": [6,12], "operand2":[6, 10]}
}

DIFFICULTY_MARKS_MAP = {
	"easy1": 30,
	"easy2": 50,
	"medium1": 60,
	"medium2": 75,
	"hard": 100,
}