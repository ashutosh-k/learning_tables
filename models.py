# encoding: utf-8

# base question class for extending any two operand question
class Question(object):
    def __init__(self, operand1, operand2, difficulty_level):
        self.operand1 = operand1
        self.operand2 = operand2
        self.difficulty_level = difficulty_level

    def __repr__(self):
        return "{} * {}".format(
            self.operand1,
            self.operand2
        )

    def __str__(self):
        return "{} * {}".format(
            self.operand1,
            self.operand2
        )

# create multiplier question class from base question class
class MultiplierQuestion(Question):
    def __init__(self, operand1, operand2, difficulty_level):
        super().__init__(operand1, operand2, difficulty_level)
        
    def check_answer(self, answer):
        return (answer == (self.operand1 * self.operand2))

# student information class
class Student(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "{}".format(
            self.name
        )

    def __str__(self):
        return "{}".format(
            self.name
        )