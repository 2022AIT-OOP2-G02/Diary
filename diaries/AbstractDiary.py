from abc import ABC, abstractclassmethod

class AbstractDiary(ABC):

    def get_date(self):
        pass

    def get_summary(self):
        pass

    def get_author(self):
        pass
