from diaries.DiarySample import DiarySample
from diaries.IzumiDiary import IzumiDiary
from diaries.KandaDiary import KandaDiary
from diaries.FukuharaDiary import FukuharaDiary


#↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    IzumiDiary(),
    KandaDiary(),
    FukuharaDiary(),
]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()