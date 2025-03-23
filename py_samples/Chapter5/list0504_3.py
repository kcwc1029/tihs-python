import random
ALP = ["A","B","C","D","E","F","G"]
r = random.choice(ALP)
alp = ""
for i in ALP:
    if i != r:
        alp = alp + i
print(alp)
ans = input("缺少哪個字母呢?")
if ans == r:
    print("答案正確")
else:
    print("答案錯誤")
