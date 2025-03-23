import random
pl_pos = 1
com_pos = 1
def banmen():
    print("・"*(pl_pos-1) + "Ｐ" + "・"*(30-pl_pos)+"Goal")
    print("・"*(com_pos-1) + "Ｃ" + "・"*(30-com_pos) +"Goal")

banmen()
print("大富翁開始！")
while True:
    input("按下Enter前進")
    pl_pos = pl_pos + random.randint(1,6)
    if pl_pos > 30:
        pl_pos = 30
    banmen()
    if pl_pos == 30:
        print("你獲勝了！")
        break
    input("按下Enter，換電腦前進")
    com_pos = com_pos + random.randint(1,6)
    if com_pos > 30:
        com_pos = 30
    banmen()
    if com_pos == 30:
        print("電腦獲勝！")
        break
