# encoding: utf-8
from random import randint
from constants import DIFFICULTY_OPERAND_MAP, DIFFICULTY_MARKS_MAP
from models import MultiplierQuestion 


class QuestionFactory:
    __instance = None

    @staticmethod 
    def getInstance():
      """ Static access method. """
      if QuestionFactory.__instance == None:
         QuestionFactory()
      return QuestionFactory.__instance

    def __init__(self):
      """ Virtually private constructor. """
      if QuestionFactory.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         QuestionFactory.__instance = self

    def get_question_generator(self, type='class_generator'):
        if type == 'class_generator':
            return QuestionGenerator()
        else:
            raise ValueError(type)


class QuestionGenerator:

    def __get_operands(self, difficulty_level):
        #generate random operands in range of defficulty level
        operand1 = randint(DIFFICULTY_OPERAND_MAP[difficulty_level]["operand1"][0],
            DIFFICULTY_OPERAND_MAP[difficulty_level]["operand1"][1])

        operand2 = randint(DIFFICULTY_OPERAND_MAP[difficulty_level]["operand2"][0],
            DIFFICULTY_OPERAND_MAP[difficulty_level]["operand2"][1])
        return operand1, operand2

    def get_multiplier_question(self, difficulty_level):

        (operand1, operand2) = self.__get_operands(difficulty_level)

        return MultiplierQuestion(operand1, operand2, difficulty_level)


class DifficultyFactory:
    __instance = None
    __difficulty_level = 'easy1'

    @staticmethod 
    def getInstance():
      """ Static access method. """
      if DifficultyFactory.__instance == None:
         DifficultyFactory()
      return DifficultyFactory.__instance

    def __init__(self):
      """ Virtually private constructor. """
      if DifficultyFactory.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         DifficultyFactory.__instance = self

    def set_difficulty_level(self, difficulty_level='easy1'):
        self.__difficulty_level = difficulty_level

    def get_difficulty_level(self):
        return self.__difficulty_level

    def increase_difficulty_level(self):
        difficulty_levels = [*DIFFICULTY_MARKS_MAP]
        index = difficulty_levels.index(self.__difficulty_level)
        if index < (len(difficulty_levels) - 1):
            self.__difficulty_level = difficulty_levels[index + 1]

    def decrease_difficulty_level(self):
        difficulty_levels = [*DIFFICULTY_MARKS_MAP]
        index = difficulty_levels.index(self.__difficulty_level)
        if index > 0:
            self.__difficulty_level = difficulty_levels[index - 1]

    def get_marks(self):
        return DIFFICULTY_MARKS_MAP[self.__difficulty_level]