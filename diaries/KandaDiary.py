from diaries.AbstractDiary import AbstractDiary

class KandaDiary(AbstractDiary):

    def get_date(self):
        return "2022-11-30"

    def get_summary(self):
        return "とても良い一日だった。課題が全て終わってよかった"
        
    def get_author(self):
        return "Kanda"