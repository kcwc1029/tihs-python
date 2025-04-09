## 1. CUI 與 GUI

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

## 2. Lab：抽卡包

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

## 3. Lab：大富翁

### 3.1. 顯示大富翁畫面

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

### 3.2. 利用迴圈推進

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

### 3.3. 判斷抵達終點

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

### 3.4. 優化為你跟電腦玩

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

## 4. Lab：尋找消失的英文字母

這是一個【時間競速的遊戲】比較看誰能找到【正確】的字母

### 4.1. 如何計時

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

### 4.2. 做字母陣列

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

### 4.3. 延伸：做字母陣列

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

### 4.4. 將所有東西做結合

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


