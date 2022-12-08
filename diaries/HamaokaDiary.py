from diaries.AbstractDiary import AbstractDiary

class HamaokaDiary(AbstractDiary):

    def get_date(self):
        return "2022-12-15"

    def get_summary(self):
        return "今日が一限があったので大変だった"
        
    def get_author(self):
        return "Hamaoka"