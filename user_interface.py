import i18n
import time
from question_generator import QuestionFactory, DifficultyFactory

class UserInterface:
    """docstring for ClassName"""
    def __init__(self):
        self.confidence = 0
        self.attemp_counts = 0
        self.difficultyFactory = DifficultyFactory.getInstance()
        self.questionGenerator = QuestionFactory.getInstance().get_question_generator()
        
    def greet_user(self):
        print(i18n.t('msg.greeting'))
        name = ''
        while not name or not name.replace(" ", "").isalpha():
            name = input(i18n.t('msg.name_input')).strip()
            # accept only alpha values
            if not name.replace(" ", "").isalpha():
                print("Invalid name.")
        return name

    def display_question(self):
        # print('difficulty_level', self.difficultyFactory.get_difficulty_level())
        question = self.questionGenerator.get_multiplier_question(self.difficultyFactory.get_difficulty_level())
        print(i18n.t('msg.question', operand1=question.operand1, operand2=question.operand2))
        start_time = time.time()
        answer = ''
        # accept only numeric values
        while not answer or not answer.isnumeric():
            answer = input(i18n.t('msg.answer_input')).strip()

        return question, answer, time.time() - start_time

    def is_answer_correct(self, question, answer):
        if len(answer) < 4:
            answer =  int(answer)
            is_correct = question.check_answer(answer)
        else:
            is_correct = False

        return is_correct

    def show_feedback(self, is_correct):
        print(i18n.t('msg.correct_answer')) if is_correct else print(i18n.t('msg.incorrect_answer'))

    def update_confidence(self, is_correct):
        self.attemp_counts += 1
        if is_correct:
            diffrential = int((self.difficultyFactory.get_marks() - self.confidence) / self.attemp_counts)
            self.confidence = self.confidence + diffrential

    def show_confidence(self):
        print(i18n.t('msg.confidence', confidence=self.confidence))

    def get_confidence(self):
        return self.confidence

    def update_difficulty_level(self, is_correct):
        if is_correct:
            self.difficultyFactory.increase_difficulty_level()
        else:
            self.difficultyFactory.decrease_difficulty_level()

    def say_goodbye(self, student):
        self.show_confidence()
        print(i18n.t('msg.goodbye', name=student))

    
