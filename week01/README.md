到這邊的話，代表你們已經安裝完了
總之，當你們成功看到這串文字時，就代表你們已經成功了 XD

![image|467x414](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250323_1742717740.png)

> [!NOTE] 補充
> 這部動畫較【Re:從零開始的異世界生活】
> 超級好看!!!

## 1. 基本輸出 print

學習每一個程式的第一步，就是要將你的程式碼給【印出來】
(讓你有種， 歐齁~電腦在聽我的話耶~ 這種感覺)
如何將程式碼運行出來呢

```python
# print(妳想要輸出的東西)

print(1+2)
print(3*5)
print(7/2)
print(7%2)
print("助教好可愛")
```

> [!info] 補充：
> 整數(int)、浮點數(float)

那如果我來做一些奇怪的事怎麼樣 ，像是ww

```py
print(10/0)
```

### 1.1. 嘗試輸出字串

我們來試試看輸出「文字」

```python
# error
你好，我是助教，今天很高興認識你

# correct
"你好，我是助教，今天很高興認識你"

# 可以用單引號或雙引號
```

### 1.2. 輸出字串月曆

阿!!!!，助教想起來，助教這個月好像要跟雷姆一起去看電影，但忘記是哪一天了(ಠ 益 ಠ)
小朋友，你可以幫我看一下這個月的時間嗎

<img src="https://i.pinimg.com/236x/b3/6b/95/b36b9501aecb662cb3cc6a4fb6421635.jpg" width="300px">

> [!NOTE] 補充：檔案(模組 module)的載入方式
> 東西不是一次載入進來，而是【需要甚麼，才載入甚麼】

因此，我們現在需要【月曆模組】我們要如何載入他呢

-   在 thonny 中安裝模組
-   在程式碼中說 我要載入【月曆模組】

```python
import calendar
# 載入後。就可以開心使用摟
```

-   使用他

```python
import calendar

# 查看2025年4月的天數
calendar.month(2025,4)

# 輸出

#      April 2025
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30
```

阿！完了，好像不是這個月，你可以再幫我把整年都掉出來嗎?

```python
import calendar

# 查看2025年所有
print(calendar.prcal(2025))
```

## 2. 變數

那其實，我們盡可能的會把我們要的東西，用一個【變數】去代表他
假設我今天要輸出的內容超級長，我總不能讓費時間在打內容本身吧 XD

<img src="https://i.pinimg.com/736x/80/c5/dc/80c5dc6e76d420402d307ff3bc98ad77.jpg" width="300px">

```python
# bad
print("從零開始的異世界生活")
print("從零開始的異世界生活")

# good
t = "從零開始的異世界生活"
print(t)
```

### 2.1. 變數命名方式

這很重要，名子取不好的話，助教就會氣到發光歐

<img src="https://i.pinimg.com/736x/0a/a9/ab/0aa9ab859dd588935dc1113db802fcbe.jpg" width="200px">

```
# correct
x = 0
gold = 1000
TA = "助教好可愛"
TA_cute = "助教好可愛"

# error
1play = 0 # 數字不可以開頭
@play = 0 # 特殊文字不可以開頭
if = 0 # 保留字不可以使用
```

## 3. 資料類型(data type)

晉賢

## 4. 輸入資料(input)

程序在執行時，會有【等待使用者】輸入的時機
我們要如何時做呢

```python
n = input("這邊可以輸入你要的資料：")
print(n)
print(type(n))

# 這邊可以輸入你要的資料：45
# 45
# <class 'str'>
```

這邊可以發現，我在讀取之後，讀取進來的資料是【string(字串)】(是不能做加減計算的)
如果我要的是，可以計算的【數值】=> 【integer(整數)】

```python
n = int(input("這邊可以輸入你要的資料："))
print(n)
print(type(n))

# 這邊可以輸入你要的資料：0123
# 123
# <class 'int'>
```

上述是提到【字串轉整數】，如果是【整數轉字串】呢

```python
n = int(input("這邊可以輸入你要的資料："))
print(type(n))
m = str(n)
print(m)
print(type(m))

# 這邊可以輸入你要的資料：16
# <class 'int'>
# 16
# <class 'str'>
```

## 5. 條件句 if/else

這是助教在【Re:從零開始的異世界生活】最喜歡的三個角色(阿還有愛姬多那)

<span>
<img src="https://i.pinimg.com/736x/91/cd/da/91cdda3fe434aacfda3c784d1ce108ab.jpg" height="400">
<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250323_1742722899.png" height="400">
</span>

因為助教平時在研究室敲鍵盤敲得好痛苦，想買個手伴，讓冷冷的桌面有一點溫興的感覺。
但是，助教因為手頭緊緊，確定無法 3 個手伴都買，那這時候，就是一個人生交叉十字路口的選擇...

這邊就是條件句使用的一個好情況：

> [!NOTE] Title
> 條件 01：如果【助教的錢錢可以買 3 隻手伴】，【助教就會很開心全買】
> 條件 02：那如果【助教的錢錢可以買 2 隻手伴】，【助教就先找雷姆跟拉姆的組合手伴】
> 條件 03：如果真的沒辦法，就【先買艾米利亞】

寫成程式的話，會長這樣

```python
# 假設一隻手伴300塊
pay = 300 # 助教的錢錢

if pay>900:
    print("可以買3隻手伴")
elif(pay>600):
    print("買雷姆跟拉姆")
else:
    print("先買一隻愛米利亞就好")

# 先買一隻愛米利亞就好
```

再舉另個例子，遊戲當中，角色的操作其實就是藉由按鍵去下不同的條件(指令)

<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250323_1742729719.png" height="500">

進賢：出 2-3 題小題目，給他們練習
做個小題目
然後輸出要長怎樣

> [!EXAMPLE] Lab：【猜燈謎遊戲】
> 我們來寫個【猜燈謎遊戲】
> 會有一個題目敘述，玩家可以輸入答案。程式會去比較玩家輸入與答案，並輸出「答對了」或「答錯了」。

```python
# Answer
ans = "圍巾"
question = "天天跟你黏一起，天冷時才想起。（猜一衣物）"

print(question)
n = input()
if n == ans:
    print("答對了")
else:
    print("答錯了")
```

> [!EXAMPLE] Lab
> 題目
> 應該要輸出甚麼

## 6. 列表

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

## 7. 迴圈

如果我今天想【跑一遍陣列】，就要使用到迴圈
迴圈的意思，就是說【要做重複的事】
迴圈有兩種，分別為：

-   for 迴圈：我知道我要【做幾次】
-   while 迴圈：只要【符合一個條件】，我就一直做

### 7.1. for 迴圈

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

### 7.2. while 迴圈

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

### 7.3. break

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

### 7.4. continue

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

## 8. 函數

函數就是把一段常常會用的動作，打包成一個你自己取的名字，以後想用就「叫名字」就好！

> 就像是煮雞湯，如果你都是從菜市場買雞肉回來熬，就是會比較麻煩。
> 如果先一次煮多一些，然後把他拿去冷凍做成雞湯塊，有需要使用，再從冷凍庫拿出來，這樣 484 會比較輕鬆

### 8.1. 函數的語法

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

### 8.2. 參數

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

### 8.3. 回傳

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
