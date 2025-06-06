## 1. 列表

> [!NOTE] 補充
> 在 python 當中，他叫列表(list)；在其他程式中，他叫陣列(array)

假如今天助教想要將大家的名字儲存起來，那你覺得助教應該怎麼做。像這樣嗎？

```python
student00 = "菜月昴"
student01 = "愛蜜莉雅"
student02 = "帕克"
student03 = "雷姆"
student04 = "拉姆"
student05 = "艾姬多娜"

print(student05) # 艾姬多娜
```

這個時候，你是不是在心裡 OS

> 如果我有 100 個，我不就要做一百次資料嗎...

助教有聽到你的疑問了~這時候，我們就要用這個東西：陣列

![image|187x186](https://i.pinimg.com/736x/21/e1/02/21e1029e0ded502d16674bb82806f051.jpg)

<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250323_1742721868.png" height="150">

> [!NOTE] 補充
>
> 其實呀，學程式這件事，他就是在電腦裡面，去做各式各樣的容器與指令
> 這邊提到的容器，指的就是裝資料的方式
> 如果未來你得的是資訊相關科系，就會碰到大名鼎鼎的課程【資料結構】

列表就像是一個超級無敵大書櫃，可以讓你放很多東東。當然，這個「大書包」也不只裝書，還可以裝各種各樣的東西（不同的資料型態）

```python
student = ["菜月昴","愛蜜莉雅","帕克","雷姆","拉姆","艾姬多娜"]

##### index #####
print(student[0]) # 菜月昴
print(student[3]) # 雷姆

print(student[-1]) # 艾姬多娜
print(student[-2]) # 拉姆

##### 切片（slice）#####
print(student[0:3]) # ['菜月昴', '愛蜜莉雅', '帕克']
print(student[3:-1]) # ['雷姆', '拉姆']

##### 修改內容 #####
student[-1]="我獨自升級"
```

### 1.1. 二維陣列

```python
arr=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(arr[0][0]) # 1
print(arr[0][-1]) # 3
print(arr[-1][0]) # 7
print(arr[0][:]) # [1, 2, 3]
```

### 1.2. 了解陣列長度

list 如果是一個容器，那知道容器長度（也就是元素數量），就變得很自然拉～

```python
student = ["菜月昴","愛蜜莉雅","帕克","雷姆","拉姆","艾姬多娜"]
print(len(student))
```

### 1.3. 列表新增元素

假設我們要將雷姆（元素）放進 list（你說為什麼要放雷姆？啊，我喜歡 ww）


![upgit_20250401_1743475285.png|219x220](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/04/upgit_20250401_1743475285.png)


```python
student = ["菜月昴","愛蜜莉雅","帕克","雷姆","拉姆","艾姬多娜"]
student.append("蕾姆")  # 新增一個學生名字
print(student)  # ["菜月昴", "愛蜜莉雅", "帕克", "雷姆", "拉姆", "艾姬多娜", "蕾姆"]

# 注意：他是在加在【列表的尾端】
```

### 1.4. 列表刪除元素

假設我們今天要把雷姆（元素）從名單中刪除。
![image|210x210](https://i.pinimg.com/474x/c3/08/1d/c3081d33bfc0d7835d1525f81bea1b90.jpg)

```python
student = ["菜月昴","愛蜜莉雅","帕克","雷姆","拉姆","艾姬多娜"]
student.remove("雷姆")  # 刪除「雷姆」
print(student)  # ["菜月昴", "愛蜜莉雅", "帕克", "拉姆", "艾姬多娜"]
```

> [!EXAMPLE] Lab：元素切片
> 【題目描述】假如你是學校餐廳的員工，你想透過寫程式，得知最後一個排隊的學生是誰？
> ```python
> students = ["菜月昴", "愛蜜莉雅", "帕克", "雷姆", "拉姆", "艾姬多娜"]
> print(f"最後一個排隊的學生是：{...}，希望他不是吃泡麵的，餐廳不提供～")
> ```
> ```python
> ##### answer #####
> students = ["菜月昴", "愛蜜莉雅", "帕克", "雷姆", "拉姆", "艾姬多娜"]
> print(f"最後一個排隊的學生是：{students[-1]}，希望他不是吃泡麵的，餐廳不提供～")
> ```


> [!EXAMPLE] Lab：元素切片
> 【題目描述】寫一個程式，輸出在陣列中間的那一位學生
> ```python
> students = ["菜月昴", "愛蜜莉雅", "帕克", "雷姆", "拉姆", "艾姬多娜"]
> middle_student = ...  # 正中央的人
> print(f"今天最焦點的學生是：{middle_student}")
> ```
> ```python
> ##### answer #####
> students = ["菜月昴", "愛蜜莉雅", "帕克", "雷姆", "拉姆", "艾姬多娜"]
> middle_student = students[len(students) // 2]  # 正中央的人
> print(f"今天最焦點的學生是：{middle_student}")
> ```



## 2. 迴圈

如果我今天想【跑一遍陣列】，就要使用到迴圈
迴圈的意思，就是說【要做重複的事】
有兩種格式：

-   for 迴圈：我知道我要【做幾次】
-   while 迴圈：只要【符合一個條件】，我就一直做

### 2.1. for 迴圈

![image|505x329](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250326_1742973023.png)
#### 2.1.1. for 迴圈--第一種表示法
適用於【明確設定次數(開頭、結尾、間隔)】
同時可以取值跟索引(索引就是【第幾個位置】)

```python
for i in range(5):
    print(f"{i} 雷姆好可愛")
    # 如果你要他不換行的話
    # print("雷姆好可愛", end=" ")

# 0 雷姆好可愛
# 1 雷姆好可愛
# 2 雷姆好可愛
# 3 雷姆好可愛
# 4 雷姆好可愛
```

```python
for i in range(1,10):
    print(f"{i} 雷姆好可愛", end=" ")

#  雷姆好可愛 2 雷姆好可愛 3 雷姆好可愛 4 雷姆好可愛 5 雷姆好可愛 6 雷姆好可愛 7 雷姆好可愛 8 雷姆好可愛 9 雷姆好可愛
```

```python
for i in range(1,10, 2):
    print(f"{i} 雷姆好可愛", end=" ")

# 1 雷姆好可愛 3 雷姆好可愛 5 雷姆好可愛 7 雷姆好可愛 9 雷姆好可愛
```

#### 2.1.2. for 迴圈--第二種表示法

適用於【跑陣列來使用】
取值更方便，但無法操作索引

```python
student = ["菜月昴","愛蜜莉雅","帕克","雷姆","拉姆","艾姬多娜"]

for i in student
	print(i, end=" ")
```

> [!EXAMPLE] Lab：遍歷字元
> 【題目描述】將字串「hello」利用 for 迴圈得方式，一個個輸出字元
>
> ```python
> word = "hello"
> for ...
> ```
>
> ```python
> ##### answer #####
> word = "hello"
> for i in word:
> 	print(i)
> ```

> [!EXAMPLE] Lab：數值加總
> 【題目描述】請利用 for 迴圈，計算 1 到 100 的加總
>
> ```python
> total = 0
> for ...
> 	...
> print(f"1-100累加為{total}")
> ```
>
> ```python
> ##### answer #####
> total = 0
> for i in range(1,101):
> 	total += i
> print(f"1-100累加為{total}")
> ```

> [!EXAMPLE] 元素新增
> 【題目描述】如果你是班長，想知道班上是否有「雷姆」這個名字
> （雷姆就跟英雄一樣，有時候會遲到，但不會不到）
>
> ```python
> students = "菜月昴", "愛蜜莉雅", "帕克", "雷姆", "拉姆", "艾姬多娜"
> name = input("（請你輸入雷姆）")
> ...
> 	print("雷姆就在這！班上找得到！")
> ...
> 	print("雷姆這學期沒來，可能她又去迷路了～")
> ```
>
> ```python
> ##### answer #####
> students = "菜月昴", "愛蜜莉雅", "帕克", "雷姆", "拉姆", "艾姬多娜"
> name = input("（請你輸入雷姆）")
> if name in students:
> 	print("雷姆就在這！班上找得到！")
> else:
> 	print("雷姆這學期沒來，可能她又去迷路了～")
> ```

> [!EXAMPLE] Lab：猜燈謎遊戲
> 【題目描述】我們要來玩一個連續的猜燈謎遊戲，題目與答案個別存在兩個 list，請你寫一段程式，去完成連續的問答，並在每一次玩家輸入後，都要告訴玩家答對或答錯。
>
> ```python
> question = [
>     "天天跟你黏一起，天冷時才想起。（猜一衣物）：",
>     "什麼東西越洗越髒：",
>     "哪一條線永遠不會有結：",
>     "你的右邊臉頰長得像什麼？：",
>     "哪尊神明不喜歡吵鬧："
> ]
>
> ans = ["圍巾", "水", "時間線", "像你的左邊臉頰", "觀世音"]
>
> for i in ...
> ```
>
> ```python
> ##### answer #####
> question = [
>     "天天跟你黏一起，天冷時才想起。（猜一衣物）：",
>     "什麼東西越洗越髒：",
>     "哪一條線永遠不會有結：",
>     "你的右邊臉頰長得像什麼？：",
>     "哪尊神明不喜歡吵鬧："
> ]
>
> ans = ["圍巾", "水", "時間線", "像你的左邊臉頰", "觀世音"]
>
> for i in range(len(question)):
>     print(question[i])
>     n = input()
>     if n == ans[i]:
>         print("答對了")
>     else:
>         print("答錯了")
> ```

> [!EXAMPLE] 寵物訓練遊戲  
> 【題目描述】你正在訓練你的寵物，它的名字是「小雷」，今天你要教牠「坐下」、「握手」和「滾動」三個動作，請你依序詢問每個動作是否學會，並印出對應訊息。
>
> ```python
> commands = ["坐下", "握手", "滾動"]
>
> for i in ...
> ```
>
> ```python
> ##### answer #####
> commands = ["坐下", "握手", "滾動"]
>
> for i in range(len(commands)):
>     print(f"教 {commands[i]} 給小雷！")
>     n = input(f"小雷學會了 {commands[i]} 嗎？(是/否): ")
>     if n == "是":
>         print(f"好樣的！小雷現在會 {commands[i]}！")
>     else:
>         print(f"沒關係！再試一次！")
> ```

#### 2.1.3. 雙重 for 迴圈

上面的例子，都是只使用一個 for 迴圈，如果我裡面在下一個 for 迴圈呢？

```python
for i in range(3):
	for j in range(5):
		print(i, j)
# 0 0
# 0 1
# 0 2
# 0 3
# 0 4
# 1 0
# 1 1
# 1 2
# 1 3
# 1 4
# 2 0
# 2 1
# 2 2
# 2 3
# 2 4
```

那雙重迴圈可以在那裡會用到呢？最經典的就是【九九乘法表】

```python
for i in range(1, 10):
	for j in range(1, 10):
		num = i*j
		print(f"{j} * {i} = {num:2} ", end=" ")
	print()

# 1 * 1 =  1  2 * 1 =  2  3 * 1 =  3  4 * 1 =  4  5 * 1 =  5  6 * 1 =  6  7 * 1 =  7  8 * 1 =  8  9 * 1 =  9
# 1 * 2 =  2  2 * 2 =  4  3 * 2 =  6  4 * 2 =  8  5 * 2 = 10  6 * 2 = 12  7 * 2 = 14  8 * 2 = 16  9 * 2 = 18
# 1 * 3 =  3  2 * 3 =  6  3 * 3 =  9  4 * 3 = 12  5 * 3 = 15  6 * 3 = 18  7 * 3 = 21  8 * 3 = 24  9 * 3 = 27
# 1 * 4 =  4  2 * 4 =  8  3 * 4 = 12  4 * 4 = 16  5 * 4 = 20  6 * 4 = 24  7 * 4 = 28  8 * 4 = 32  9 * 4 = 36
# 1 * 5 =  5  2 * 5 = 10  3 * 5 = 15  4 * 5 = 20  5 * 5 = 25  6 * 5 = 30  7 * 5 = 35  8 * 5 = 40  9 * 5 = 45
# 1 * 6 =  6  2 * 6 = 12  3 * 6 = 18  4 * 6 = 24  5 * 6 = 30  6 * 6 = 36  7 * 6 = 42  8 * 6 = 48  9 * 6 = 54
# 1 * 7 =  7  2 * 7 = 14  3 * 7 = 21  4 * 7 = 28  5 * 7 = 35  6 * 7 = 42  7 * 7 = 49  8 * 7 = 56  9 * 7 = 63
# 1 * 8 =  8  2 * 8 = 16  3 * 8 = 24  4 * 8 = 32  5 * 8 = 40  6 * 8 = 48  7 * 8 = 56  8 * 8 = 64  9 * 8 = 72
# 1 * 9 =  9  2 * 9 = 18  3 * 9 = 27  4 * 9 = 36  5 * 9 = 45  6 * 9 = 54  7 * 9 = 63  8 * 9 = 72  9 * 9 = 81
```

### 2.2. while 迴圈

![image|648x242](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250326_1742973796.png)

```python
num = 1
while num<5:
    print(f"{num} 雷姆好可愛")
    num += 1 # num = num + 1

# 1 雷姆好可愛
# 2 雷姆好可愛
# 3 雷姆好可愛
# 4 雷姆好可愛
```

> [!danger]
> while 迴圈有一個很危險的動作，請大家一定要注意
> while 迴圈的條件，一定要滿足，他才會結束；如果沒有讓它結束，他就會一直一直一直做同一件事 => 無限迴圈(這是很不好的！！！)

```python
# 這行讓助教先示範，不要自己操作
num = 1
while num<5:
    print(f"{num} 雷姆好可愛")
```

> [!EXAMPLE] Lab：無限喝奶茶大作戰
> 你是一個奶茶控，每天都要喝上一杯奶茶。不過，現在有一個問題——你到底喝了多少杯呢？讓我們來看看這個「無限」喝奶茶的故事...
>
> ```python
> cups = 0
> while cups < 5:
>     print(f"喝了 {cups + 1} 杯奶茶！")
>     cups += 1
> ```

### 2.3. break

![image|706x253](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250326_1742974148.png)

```python
num = 0
while num<5:
    if num ==3:
        break
    print(f"{num} 雷姆好可愛")
    num += 1 # num = num + 1

# 0 雷姆好可愛
# 1 雷姆好可愛
# 2 雷姆好可愛
```

> [!EXAMPLE] 寶可夢捕捉計劃
> 你正在進行一個寶可夢捕捉計劃。你的目標是捕捉一定數量的寶可夢。但是當你捕捉到最想要的那隻寶可夢後，你就決定停止。
>
> ```python
> pokemon = 0
> while pokemon < 10:
>     if pokemon == 5:  # 當捕捉到第 5 隻寶可夢時就停止
>         print("捕捉到最想要的寶可夢，停下來休息！")
>         break
>     print(f"捕捉到第 {pokemon + 1} 隻寶可夢")
>     pokemon += 1
> ```

### 2.4. continue

```python
num = 0
while num < 5:
    if num == 3:
        num += 1  # 先加，再跳過
        continue
    print(f"{num} 雷姆好可愛")
    num += 1

# 0 雷姆好可愛
# 1 雷姆好可愛
# 2 雷姆好可愛
# 4 雷姆好可愛
```

<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250326_1742974688.png" height="400">


> [!EXAMPLE] 早起大挑戰
> 【題目描述】你今天決定早起去跑步，目標是運動 5 天。
> - 天氣只會有兩種選擇（晴天/下雨）
> - 如果今天是下雨，就要輸出"今天下雨，跳過跑步！"
> - 如果今天是晴天，就要輸出""今天運動完成！已經跑了 XX 天""
> 
> ```python
> days = 0
> while days < 5:
>     print("今天下雨，跳過跑步！")
>     print(f"今天運動完成！已經跑了...天")
> ```
> ```python
> ##### answer #####
> days = 0
> while days < 5:
>     weather = input("今天天氣如何（晴天/下雨）？")
>     if weather == "下雨":
>         print("今天下雨，跳過跑步！")
>         days += 1  # 即便天氣不好，還是算完成一天
>         continue
>     print(f"今天運動完成！已經跑了 {days + 1} 天")
>     days += 1
> ```



> [!EXAMPLE] 一天三餐挑戰
> 【題目描述】你今天決定要記錄自己有沒有吃三餐（早餐、午餐、晚餐），請寫一段程式，會：
> 1. 按照順序問使用者：「有沒有吃早餐？」、「有沒有吃午餐？」、「有沒有吃晚餐？」 
> 2. 如果使用者輸入「是」，就顯示：「已記錄：早餐（或午餐／晚餐）」。
> 3. 如果使用者輸入「否」，就顯示：「沒吃早餐（或午餐／晚餐），跳過！」。
> 4. 不論吃沒吃，都要繼續問下一餐。
> 【範例互動（可能的輸出）：】
> ```
> 今天有吃 早餐 嗎？(是/否) 否
> 沒吃 早餐，跳過！
> 今天有吃 午餐 嗎？(是/否) 是
> 記錄下 午餐 完成！
> 今天有吃 晚餐 嗎？(是/否) 是
> 記錄下 晚餐 完成！
> ```
> ```python
> meals = ["早餐", "午餐", "晚餐"]
> meal_count = 0
> 
> while ...
> ```
> 
> ```python
> ##### answer #####
> meals = ["早餐", "午餐", "晚餐"]
> meal_count = 0
> 
> while meal_count < len(meals):
>     meal = input(f"今天有吃 {meals[meal_count]} 嗎？(是/否) ")
>     if meal == "否":
>         print(f"沒吃 {meals[meal_count]}，跳過！")
>         meal_count += 1
>         continue  # 跳過當天的餐點，進入下一餐
>     print(f"記錄下 {meals[meal_count]} 完成！")
>     meal_count += 1
> ```


## 3. 函數

函數就是把一段常常會用的動作，打包成一個你自己取的名字，以後想用就「叫名字」就好！

> 就像是煮雞湯，如果你都是從菜市場買雞肉回來熬，就是會比較麻煩。
> 如果先一次煮多一些，然後把他拿去冷凍做成雞湯塊，有需要使用，再從冷凍庫拿出來，這樣 484 會比較輕鬆

### 3.1. 函數的語法

分為「定義函數」跟「呼叫函數」

```python
##### 定義函數 #####
def cute():
	# 這個函數要做的事
	print("雷姆好可愛")

##### 呼叫函數 #####
cute() # 雷姆好可愛
cute() # 雷姆好可愛
cute() # 雷姆好可愛
cute() # 雷姆好可愛
cute() # 雷姆好可愛
```

再用【煮雞湯】舉個例

```python
##### 定義函數 #####
def chicken_soup():
	# 這個函數要做的事
	print("備料")
	print("汆燙雞肉")
	print("加水煮湯")
	print("轉小火慢燉")
	print("調味與撈油")


##### 主程式 #####
chicken_soup() # 雷姆好可愛
```


> [!EXAMPLE] 追劇計劃生成器
> 假設你有一個追劇計劃，每週要看 5 集，你希望能每週安排不同的劇集。這時候，你可以利用函數來幫助自己計劃每週的觀看進度。
>
> ```python
> # 這個函數會生成每週看劇的計劃
> def weekly_show_plan(week_number):
>     for i in range(1, 6):  # 每週 5 集
>         print(f"第{week_number}週，觀看劇集 {i} 集")
>
> # 主程式
> weekly_show_plan(1)
> weekly_show_plan(2)
> weekly_show_plan(3)
> ```

### 3.2. 參數

在認識完基本函數後，我們來做個不一樣的變化
假設我今天要做一個函數，這個函數的任務是【接收兩個數字，然後把兩數相加，這個數字就是決定，輸出“拉姆好可愛”的次數】

```python
def cute(a, b):
    c = a + b
    for i in range(c):
        print("拉姆好可愛")
    print()

##### 主程式 #####
cute(1, 0)

cute(a=1, b=2)
```

那其實你可以發現，cute()他裡面就是做兩件事

-   做加法
-   輸出

那狠一點，可以把兩件事都去做成函數

```python
##### 函數：輸出 #####
def while_print(num):
    i = 0
    while i<num:
        print(f"{i} 拉姆好可愛")
        i+=1
    print()

##### 相加 #####
def cute(a, b):
    c = a + b
    while_print(c)


##### 主程式 #####
cute(1, 0)

cute(a=1, b=2)
```


> [!EXAMPLE] 早餐時間表
> 今天早上你要吃三種不同的食物，但你還不確定每一個食物的吃法。你可以用函數來設定每個食物的吃法，然後生成今天的早餐計劃。
>
> ```python
> # 這個函數會根據輸入的食物，決定怎麼吃
> def breakfast(food1, food2, food3):
>     print(f"今天的早餐計劃：")
>     print(f"1. {food1}：先放微波爐加熱")
>     print(f"2. {food2}：加點果醬再吃")
>     print(f"3. {food3}：配上一杯牛奶")
>
> # 主程式
> breakfast("吐司", "煎蛋", "沙拉")
> ```

> [!EXAMPLE] 一周健身計劃
> 【題目描述】你想建立一個「一週健身計劃」，每週運動幾天由使用者決定，每天要做的運動從固定清單中依序選擇。請寫一個函數 `weekly_exercise(days)`，根據天數列出當天要做的運動。
> ```
> ##### 範例輸出 #####
> 第1天：做深蹲！
> 第2天：做伏地挺身！
> 第3天：做游泳！
> 第4天：做瑜伽！
> 第5天：做跑步！
> ```
> ```python
> 
> # 這個函數接收每週運動天數並列出每天的運動項目
> def weekly_exercise(days):
> 	exercises = "跑步", "深蹲", "伏地挺身", "游泳", "瑜伽"
> 	for ...
> 	...
> 	print(f"第{day}天：做{exercise}！")
> 
> # 主程式
> weekly_exercise(5)
> ```
> 
> ```python
> ##### answer #####
> # 這個函數接收每週運動天數並列出每天的運動項目
> def weekly_exercise(days):
> 	exercises = "跑步", "深蹲", "伏地挺身", "游泳", "瑜伽"
> 	for day in range(1, days + 1):
> 	exercise = exercisesday % len(exercises)
> 	print(f"第{day}天：做{exercise}！")
> 
> # 主程式
> weekly_exercise(5)
> ```

### 3.3. 回傳

目前的函數，大概是長這樣
<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250326_1742981486.png" height="300">

那~我希望他是，呼叫函數之後，函數執行完的結果，可以傳回主程式（或是在傳給其他函數）

<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250326_1742981721.png" height="300">

```python
##### 函數：輸出 #####
def while_print(num):
    i = 0
    while i<num:
        print(f"{i} 拉姆好可愛")
        i+=1
    print()

##### 相加 #####
def cute(a, b):
    c = a + b
    return c

##### 主程式 #####
temp = cute(1, 1)
ans = cute(temp, temp)
while_print(ans)

# 0 拉姆好可愛
# 1 拉姆好可愛
# 2 拉姆好可愛
# 3 拉姆好可愛
```

## 4. 亂數(random)

在遊戲中，我們會常常使用到【亂數】J 個概念，像是

-   隨機生成敵人位置
-   猜數字
-   抽卡牌

要製作函數，我們需要引入函數庫【random】（還記得嗎 XD

<img src="https://i.pinimg.com/736x/79/56/a2/7956a235970913d5edcd44492b56b0a9.jpg" width="300px">

### 4.1. 產出【介於 0-1】的亂數

```python
import random

r = random.random()
print(r)
```

### 4.2. 產出【整數】的亂數

```python
import random

r = random.randint(1,6) # 產出借於1-6之間得整數
print(r)
```

### 4.3. 產出【整數】的亂數

語法：random.randint(min, max)

```python
import random

r = random.randint(1,6) # 產出借於1-6之間得整數
print(r)
```

### 4.4. 從多個項目中中挑選出一個

如果今天要生成的東西，是有一個範圍的（像是從角色群中挑選一個角色出來）

以猜拳為例：

-   剪刀、石頭、布
-   像助教是邊緣可達鴨，沒人跟我玩(哭)

<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250326_1742983287.png" width="300px">

```python
import random

r = random.randint(1,6) # 產出借於1-6之間得整數
print(r)
```








