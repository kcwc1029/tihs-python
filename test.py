question = [
    "天天跟你黏一起，天冷時才想起。（猜一衣物）：",
    "什麼東西越洗越髒：",
    "哪一條線永遠不會有結：",
    "你的右邊臉頰長得像什麼？：",
    "哪尊神明不喜歡吵鬧："	
]

ans = ["圍巾", "水", "時間線", "像你的左邊臉頰", "觀世音"]

for i in range(len(question)):
    print(question[i])
    n = input()
    if n == ans[i]:
        print("答對了")
    else:
        print("答錯了")
