import random
cnt = 0
while True:
    r = random.randint(1, 100)
    print(r)
    cnt = cnt + 1
    if r == 77:
        break
print("於第"+str(cnt)+"次抽中超稀有角色")
