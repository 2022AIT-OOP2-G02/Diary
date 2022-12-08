from diaries.AbstractDiary import AbstractDiary

class FukuharaDiary(AbstractDiary):

    def get_date(self):
        return "2022-12-15"

    def get_summary(self):
        return "Githubタノシイ"
        
    def get_author(self):
        return "福原"