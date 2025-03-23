QUESTION = [
"蠑螈太太的老公叫什麼名字？",
"磯野鰹的妹妹叫什麼名字？",
"鱈男是磯野鰹的誰？"]
R_ANS = ["鱒男", "磯野裙帶菜", "外甥"]
for i in range(3):
    print(QUESTION[i])
    ans = input()
    if ans == R_ANS[i]:
        print("答對了")
    else:
        print("答錯了")
