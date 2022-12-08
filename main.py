from diaries.DiarySample import DiarySample
from diaries.IzumiDiary import IzumiDiary
from diaries.KandaDiary import KandaDiary
from diaries.FukuharaDiary import FukuharaDiary
from diaries.ShimizuDiary import ShimizuDiary


#↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    IzumiDiary(),
    KandaDiary(),
    FukuharaDiary(),
    ShimizuDiary(),
]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
