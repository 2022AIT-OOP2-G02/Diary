from diaries.AbstractDiary import AbstractDiary

class ShimizuDiary(AbstractDiary):

    def get_date(self):
        return "2022-12-02"

    def get_summary(self):
        return "物理実験のレポート提出がほんとにギリギリで危なかった"

    def get_author(self):
        return "Shimizu"
