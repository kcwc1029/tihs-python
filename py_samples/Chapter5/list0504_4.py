import random
import datetime
ALP = ["A","B","C","D","E","F","G"]
r = random.choice(ALP)
alp = ""
for i in ALP:
    if i != r:
        alp = alp + i
print(alp)
st = datetime.datetime.now()
ans = input("缺少哪個字母呢?")
if ans == r:
    print("答案正確")
    et = datetime.datetime.now()
    print((et-st).seconds)
else:
    print("答案錯誤")
