from diaries.DiarySample import DiarySample
from diaries.IzumiDiary import IzumiDiary
from diaries.KandaDiary import KandaDiary
from diaries.FukuharaDiary import FukuharaDiary
from diaries.ShimizuDiary import ShimizuDiary
from diaries.HamaokaDiary import HamaokaDiary
from diaries.OomoriDiary import OomoriDiary

#↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(), 
    DiarySample(),
    IzumiDiary(),
    KandaDiary(),
    FukuharaDiary(),
    ShimizuDiary(),
    HamaokaDiary(),
    OomoriDiary(),
]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
