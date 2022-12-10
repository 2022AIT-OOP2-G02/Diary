from diaries.AbstractDiary import AbstractDiary

class MotokiDiary(AbstractDiary):
    
    def get_date(self):
        return "2022-12-08"

    def get_summary(self):
        return"バイトを頑張った"

    def get_author(self):
        return "motoki"