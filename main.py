from diaries.DiarySample import DiarySample
from diaries.ShimizuDiary import ShimizuDiary

#↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    ShimizuDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
