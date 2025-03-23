import random
import datetime
ALP = [
"A","B","C","D","E","F","G",
"H","I","J","K","L","M","N",
"O","P","Q","R","S","T","U",
"V","W","X","Y","Z"
]
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
    print("總共花了"+str((et-st).seconds)+"秒喲")
else:
    print("答案錯誤")
