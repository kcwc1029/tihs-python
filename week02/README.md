
## 7. 列表

> [!NOTE] 補充
> 在 python 當中，他叫列表(list)
> 在其他程式中，他叫陣列(array)

今天助教想要將大家的名字儲存起來，那你覺得助教應該怎麼做
像這樣嗎？

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

助教有聽到你的疑問了~。這時候，我們又要用這個東西：陣列

<img src="https://i.pinimg.com/736x/21/e1/02/21e1029e0ded502d16674bb82806f051.jpg" height="300">

<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250323_1742721868.png" height="150">

> [!NOTE] 補充
>
> 其實呀，學程式這件事，他就是在電腦裡面，去做各式各樣的容器與指令
> 這邊提到的容器，指的就是裝資料的方式
> 如果未來你得的是資訊相關科系，就會碰到大名鼎鼎的課程【資料結構】

```python
student = ["菜月昴","愛蜜莉雅","帕克","雷姆","拉姆","艾姬多娜"]

print(student[0]) # 菜月昴
print(student[3]) # 雷姆

print(student[-1]) # 艾姬多娜
print(student[-2]) # 拉姆
```

進賢：利用 if else+list 出 2-3 題小題目，給他們練習

> [!EXAMPLE]
>
> 應該要輸出甚麼

> [!EXAMPLE] Lab
> 題目
> 應該要輸出甚麼

## 8. 迴圈

如果我今天想【跑一遍陣列】，就要使用到迴圈
迴圈的意思，就是說【要做重複的事】
迴圈有兩種，分別為：

-   for 迴圈：我知道我要【做幾次】
-   while 迴圈：只要【符合一個條件】，我就一直做

### 8.1. for 迴圈

<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250326_1742973023.png" height="400">

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

進賢：利用 for 出 2 題小題目，給他們練習

> [!EXAMPLE] Lab：【猜燈謎遊戲】
> 如果我們今天要做的猜燈謎遊戲，我想要一次玩 5 關呢

```python
question = [
    "天天跟你黏一起，天冷時才想起。（猜一衣物）",
    "什麼東西越洗越髒",
    "哪一條線永遠不會有結",
    "你的右邊臉頰長得像什麼？",
    "哪尊神明不喜歡吵鬧"
]

ans = ["圍巾","水","時間線", "像你的左邊臉頰", "觀世音"]

for i in range(len(question)):
    print(question[i])
    n = input()
    if n == ans[i]:
        print("答對了")
    else:
        print("答錯了")
```

> [!EXAMPLE] Lab
> 題目
> 應該要輸出甚麼

### 8.2. while 迴圈

<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250326_1742973796.png" height="400">

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

while 迴圈有一個很危險的動作，請大家一定要注意
while 迴圈的條件，一定要滿足，他才會結束；如果沒有讓它結束，他就會一直一直一直做同一件事 => 無限迴圈(這是很不好的！！！)

```python
# 這行讓助教先示範，不要自己操作
num = 1
while num<5:
    print(f"{num} 雷姆好可愛")
```

晉賢

> [!EXAMPLE] Lab
> 題目
> 應該要輸出甚麼

> [!EXAMPLE] Lab
> 題目
> 應該要輸出甚麼

### 8.3. break

<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250326_1742974148.png" height="400">

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

進賢：利用 for 出 2 題小題目，給他們練習

> [!EXAMPLE] Lab
> 題目
> 應該要輸出甚麼

> [!EXAMPLE] Lab
> 題目
> 應該要輸出甚麼

### 8.4. continue

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

進賢：利用 for 出 2 題小題目，給他們練習

> [!EXAMPLE] Lab
> 題目
> 應該要輸出甚麼

> [!EXAMPLE] Lab
> 題目
> 應該要輸出甚麼

## 9. 函數

函數就是把一段常常會用的動作，打包成一個你自己取的名字，以後想用就「叫名字」就好！

> 就像是煮雞湯，如果你都是從菜市場買雞肉回來熬，就是會比較麻煩。
> 如果先一次煮多一些，然後把他拿去冷凍做成雞湯塊，有需要使用，再從冷凍庫拿出來，這樣 484 會比較輕鬆

### 9.1. 函數的語法

-   分為「定義函數」跟「呼叫函數」

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

-   再用【煮雞湯】舉個例

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

進賢：利用 for 出 2 題小題目，給他們練習

> [!EXAMPLE] Lab
> 題目
> 應該要輸出甚麼

### 9.2. 參數

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

進賢：利用 for 出 2 題小題目，給他們練習

> [!EXAMPLE] Lab
> 題目
> 應該要輸出甚麼

### 9.3. 回傳

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

進賢：利用 for 出 2 題小題目，給他們練習

> [!EXAMPLE] Lab
> 題目
> 應該要輸出甚麼



## 1. 亂數(random)

在遊戲中，我們會常常使用到【亂數】J 個概念，像是

-   隨機生成敵人位置
-   猜數字
-   抽卡牌

要製作函數，我們需要引入函數庫【random】（還記得嗎 XD

<img src="https://i.pinimg.com/736x/79/56/a2/7956a235970913d5edcd44492b56b0a9.jpg" width="300px">

### 1.1. 產出【介於 0-1】的亂數

```python
import random

r = random.random()
print(r)
```

### 1.2. 產出【整數】的亂數

```python
import random

r = random.randint(1,6) # 產出借於1-6之間得整數
print(r)
```

### 1.3. 產出【整數】的亂數

語法：random.randint(min, max)

```python
import random

r = random.randint(1,6) # 產出借於1-6之間得整數
print(r)
```

### 1.4. 從多個項目中中挑選出一個

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

## 2. CUI 與 GUI

孩子們，這邊想問一下，在你們心中，電腦是甚麼樣子？

是這樣嗎？

<span>
<img src="https://i.pinimg.com/736x/13/e4/f9/13e4f9058fbd616f5921cd7322175d68.jpg" height="300px">
<img src="https://i.pinimg.com/236x/53/59/8a/53598abc80aa3267e7e8a0f77b4c6ce9.jpg" height="300px">
</span>

<span>
<img src="https://i.pinimg.com/736x/dd/be/11/ddbe11d4db63dcc1f638b5ceb23e9bfd.jpg" height="300px">
<img src="https://pic.3h3.com/up/2021-2/202102241033447482.jpg" height="300px">
</span>

其實電腦的本身是屬於 CUI(character user interface，字元使用者介面)（像是 python 的 shell），就是透過文字與指令來操控電腦。
但這樣是不是看起來很可怕，也很不近人情，因此工程師就在寫一個圖形介面程序，將 CUI 轉成 GUI(Graphical User Interface)。這有兩個影響點

-   使用上更加親民
-   效率會比較差(因為中間多了一到手續)

![upgit_20250326_1742985952.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250326_1742985952.png)

也因此，我們所看到的遊戲，他就是在 GUI 下面的產物。

<span>
<img src="https://i.pinimg.com/736x/d4/5e/f4/d45ef4f4e7eb8201124d3343fffc5aaa.jpg" height="300px">
<img src="https://i.pinimg.com/736x/b4/ba/ca/b4baca019140e1c8ce6cf5cdb7b7890e.jpg" height="300px">
</span>

阿，但但但，這樣的一個遊戲，其實已經不單單是只有程式了，還有遊戲美術，企劃等等。
若我們只想聚焦於程式這一塊的話，也是可以，但就是，做出來不會到那麼好看。
所以，我們會聚焦在遊戲的一個邏輯，並用 CUI 的方式去完成。

## 3. Lab：抽卡包

<img src="https://down-tw.img.susercontent.com/file/tw-11134207-7rasm-m1smlgx827t7b4@resize_w450_nl.webp" height="300px">

假設 SSR 抽取機率為 1%，意旨「抽 100 次只會有 1 次的機會會中」。或許有些人的理解是「那我只要抽 100 次，就一定會中」。那~是這樣嗎？
所謂的 1%，還是會有人抽一次就中(歐皇)，還是會有人抽 200-300 次還是不中。
接著，就讓我們來實作看看這種機制：

> 我們稍微改一下
> 將機率訂為 10%，就是「抽 10 次只會有 1 次的機會會中」之機率。

```python
import random

count = 0 # 紀錄抽取次數
while True:
    # 次數+1
    count +=1

    # 由亂數生成
    r = random.randint(1, 10)
    print(r)
    if r == 7:
        break
    print(f"於第{r}次抽中SSR")
```

> [!INFO] RPG 中設計「逃跑失敗率」的邏輯
> 在許多 RPG 遊戲中，玩家從戰鬥中選擇「逃跑」時，不一定能成功，會依照「失敗機率」決定是否逃脫成功。
> 這背後其實是一個簡單但極具彈性的機率系統設計問題。
>
> #####為什麼需要設計逃跑失敗機率#####
>
> -   增加遊戲的 緊張感與挑戰性
> -   防止玩家「輕易逃脫 → 無敵解法」
> -   符合戰鬥策略設計（有風險就會更刺激）
>
> 假設遊戲設定為【如果玩家選擇撤退，失敗機率要 33%(1/3)】
> 我們可以先隨機產生一個數字(介於 1-100)
> 如果數值在 30 以內(<30) => 撤退失敗
> 反之(30-70) => 撤退成功
>
> 【資料補充】[【專欄】論述「JRPG」在戰鬥系統上的「變」與「不變」 - 巴哈姆特](https://gnn.gamer.com.tw/detail.php?sn=161035)

## 4. Lab：大富翁

### 4.1. 顯示大富翁畫面

大富翁是邊丟骰子一邊往前的遊戲，如果我們要用 CUI 的方式去表現的話。

```
起點*****A************************終點
起點**B***************************終點
```

要如何透過程式去實做出來呢？

```python
a_pos = 6 # A的位置
b_pos = 3 # B的位置
all_pos = 30 # 地圖路徑

def f(a, b, all):
    print("起點" + "*" * (a-1) + "A" + "*" * (all-a) + "終點")
    print("起點" + "*" * (b-1) + "B" + "*" * (all-b) + "終點")

##### 主程式 #####
f(a_pos, b_pos, all_pos)
```

### 4.2. 利用迴圈推進

我想要做到：

-   按下【enter】後，他會往前進

```python
a_pos = 1 # A的位置
b_pos = 1 # B的位置
all_pos = 30 # 地圖路徑

def f(a, b, all):
    print("起點" + "*" * (a-1) + "A" + "*" * (all-a) + "終點")
    print("起點" + "*" * (b-1) + "B" + "*" * (all-b) + "終點")

##### 主程式 #####
while True
	f(a, b, all)
	input("按下enter就會前進")
	a+=1
	b+=1
```

### 4.3. 判斷抵達終點

```python
a_pos = 1 # A的位置
b_pos = 1 # B的位置
all_pos = 30 # 地圖路徑

def f(a, b, all):
    print("起點" + "*" * (a-1) + "A" + "*" * (all-a) + "終點")
    print("起點" + "*" * (b-1) + "B" + "*" * (all-b) + "終點")

##### 主程式 #####
while True:
    f(a_pos, b_pos, all_pos)
    input("按下enter就會前進")
    a_pos+=1
    b_pos+=1
    # 判斷終點
    if a_pos >= all_pos:
        a_pos = all_pos
    if b_pos >= all_pos:
        b_pos = all_pos
```

### 4.4. 優化為你跟電腦玩

```python
import random

a_pos = 1 # A的位置
b_pos = 1 # B的位置
all_pos = 30 # 地圖路徑

def f(a, b, all):
    print("起點" + "*" * (a-1) + "玩家" + "*" * (all-a) + "終點")
    print("起點" + "*" * (b-1) + "電腦" + "*" * (all-b) + "終點")


##### 主程式 #####
while True:
    f(a_pos, b_pos, all_pos)
    input("按下enter就會前進")
    a_pos+= random.randint(1, 10)
    b_pos+= random.randint(1, 10)
    # 判斷終點
    if a_pos >= all_pos:
        a_pos = all_pos
        print("玩家獲勝")
        break
    if b_pos >= all_pos:
        b_pos = all_pos
        print("電腦獲勝")
        break
```

## 5. Lab：尋找消失的英文字母

這是一個【時間競速的遊戲】比較看誰能找到【正確】的字母

### 5.1. 如何計時

首先，我們要先學會，如何計時

```python
import datetime

# 開始時間做一個標記
start = datetime.datetime.now()
for i in range(50):
    print("助教好可愛")

# 結束時間做一個標記
end = datetime.datetime.now()

print(f"開始時間{start}")
print(f"結束時間{end}")
print(f"時間差距{end-start}")
```

### 5.2. 做字母陣列

將 C 作為要消失的字母

```python
ABC = ["A", "B", "C", "D", "E", "F", "G"]
disappear = "C" # 我要消失的字母
new_ABC = []

#  做出題目
for i in ABC:
    if i != disappear:
        new_ABC.append(i)
print(new_ABC)
```

### 5.3. 延伸：做字母陣列

接下來，我要要用隨機的方式，決定要消失的字母

```python
import random

# 增強他的隨機效果
# import time
# random.seed(time.time())

ABC = ["A", "B", "C", "D", "E", "F", "G"]
disappear = random.choice(ABC) # 我要消失的字母
new_ABC = []

#  做出題目
for i in ABC:
    if i != disappear:
        new_ABC.append(i)
print(new_ABC)
```

### 5.4. 將所有東西做結合

```python
import datetime
import random

# 開始時間做一個標記
start = datetime.datetime.now()

# 增強他的隨機效果
# import time
# random.seed(time.time())

ABC = ["A", "B", "C", "D", "E", "F", "G"]
disappear = random.choice(ABC) # 我要消失的字母
new_ABC = []

#  做出題目
for i in ABC:
    if i != disappear:
        new_ABC.append(i)
print(new_ABC)

# 讓玩家輸入
ans = input("缺少哪一個字母呢？")
if ans == disappear:
    print("答對了")
else:
    print("答錯了")

# 結束時間做一個標記
end = datetime.datetime.now()
print(f"遊戲時間{end-start}")
```
