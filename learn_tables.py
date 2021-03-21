# encoding: utf-8
import os
import i18n
from models import Student
from user_interface import UserInterface
from logger import LoggerInterface

tanslation_path = os.getcwd()+'/locales'
i18n.load_path.append(tanslation_path)


userInterface = UserInterface()
loggerInterface = LoggerInterface.getInstance()
name = userInterface.greet_user()
student = Student(name)
loggerInterface.initialize_logging(student)

show_question = 'Y'
while show_question == 'Y':
    question, answer, time_taken = userInterface.display_question()
    is_correct = userInterface.is_answer_correct(question, answer)
    userInterface.show_feedback(is_correct)
    userInterface.update_confidence(is_correct)
    userInterface.update_difficulty_level(is_correct)

    loggerInterface.log("{operand1} * {operand2},{answer},{correct},{time_taken}".format(
        operand1=question.operand1,
        operand2=question.operand2,
        answer=answer,
        correct='Yes' if is_correct else 'No',
        time_taken=time_taken
    ))

    show_question = input(i18n.t('msg.play_more')).strip()
    if show_question == 'N':
        userInterface.say_goodbye(student)
        exit(1)
    else:
        show_question = 'Y'