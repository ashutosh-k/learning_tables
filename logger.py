import os
import time
import logging

class LoggerInterface:

    __instance = None

    @staticmethod 
    def getInstance():
      """ Static access method. """
      if LoggerInterface.__instance == None:
         LoggerInterface()
      return LoggerInterface.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if LoggerInterface.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            LoggerInterface.__instance = self
    
    def initialize_logging(self, student):
        self.lgr = logging.getLogger('learning tables')
        self.lgr.setLevel(logging.INFO)
        # create file handler for logging
        fh = logging.FileHandler(os.getcwd()+'/logs/{name}_{timestamp}.csv'.format(name=student, timestamp=time.time()))
        fh.setLevel(logging.INFO)
        frmt = logging.Formatter('%(message)s')
        fh.setFormatter(frmt)

        # add the Handler to the logger
        self.lgr.addHandler(fh)
        self.log("Question,Answer,Correct,Time Taken To Answer")

    def log(self, message):
        self.lgr.info(message)
