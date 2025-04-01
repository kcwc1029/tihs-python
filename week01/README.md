## 1. thonny IDE

【我們要用 python 寫程式】，那這句話當中，你可能會有兩個名詞不太懂，Python 是甚麼？程式是甚麼？

這樣說好了，假設我們要煮飯：

-   煮飯是一個動作(就是寫程式)
-   然後我們會需要白米(就是 python)
-   我們需要電鍋(這個就是 IDE)
    -   煮飯可以有很多方式，可以用電鍋，可以自己炊 etc，IDE 也是依樣。

這次這次我們選的電鍋(IDE)就是 thonny

![upgit_20250331_1743413474.png|268x271](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250331_1743413474.png)

### 1.1. 安裝 thonny

安裝連結：[Thonny, Python IDE for beginners](https://thonny.org/)

![upgit_20250331_1743411768.png|614x436](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250331_1743411768.png)

就是一直預設安裝即可(簡單八)

![upgit_20250331_1743411857.png|445x341](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250331_1743411857.png)![upgit_20250331_1743411918.png|430x341](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250331_1743411918.png)

### 1.2. 使用 thonny

![upgit_20250331_1743413294.png|158x158](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250331_1743413294.png)

這樣就安裝好搂！讓我們來啟動她

![upgit_20250331_1743412154.png|481x454](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250331_1743412154.png)

在打開後，他會長這樣(可能顏色會不同，但基本版面都是這樣)

![upgit_20250331_1743412241.png|604x392](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250331_1743412241.png)

首先，我們要對電鍋做一些設定參數
IDE 他本身是一個編輯器環境，我們要告訴他，要用【python】寫程式

![upgit_20250331_1743412830.png|508x259](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250331_1743412830.png)

![upgit_20250331_1743412877.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250331_1743412877.png)

我們來簡單介紹一下這個 IDE 版面跟操作

![upgit_20250331_1743413103.png|571x374](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250331_1743413103.png)

1 號區塊就是檔案路徑，就跟你的檔案總館一樣

![upgit_20250331_1743413160.png|531x395](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250331_1743413160.png)

2 號區塊就是讓你寫程式的地方
3 號區塊就是程式執行，顯示結果的地方

那接下來幫我在【2 好區塊】寫下這一串

```python
print("hello 南工", 123)
```

![upgit_20250331_1743413656.png|790x174](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250331_1743413656.png)

要讓程式運行，就按綠色按鈕(要記得儲存(ctrl+S)
要讓程式停止，就按紅色按鈕

![upgit_20250331_1743413733.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250331_1743413733.png)

到這邊的話，代表你們已經安裝完了
總之，當你們成功看到這串文字時，就代表你們已經成功了 XD

![image|467x414](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250323_1742717740.png)

> [!NOTE] 補充
> 這部動畫較【Re:從零開始的異世界生活】
> 超級好看!!!

## 2. 基本輸出 print

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

那如果我來做一些奇怪的事怎麼樣 ，像是 ww

```py
print(10/0)
```

![upgit_20250331_1743413805.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250331_1743413805.png)

> [!error] 他報錯了
> 上一次看到紅色的東西，應該是校門口的紅綠燈對吧
> 紅色通常就是告訴你，遇到了一些錯誤，請你去把這個錯誤處理掉！！

### 2.1. 嘗試輸出字串

我們來試試看輸出「文字」

```python
# error
你好，我是助教，今天很高興認識你

# correct
"你好，我是助教，今天很高興認識你"

# 可以用單引號或雙引號
```

### 2.2. 輸出字串月曆

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

## 3. 變數

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

### 3.1. 變數命名方式

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

## 4. 資料類型(data type)

在 Python 裡，每一個變數，都有一個屬性：資料類型
就像每個角色都有職業一樣（劍士、魔法師、補師），不同的資料型態，能做的事情也不一樣！

| 資料型態        | 範例              | 說明                 |
| --------------- | ----------------- | -------------------- |
| `int`（整數）   | `123`, `-7`, `0`  | 不帶小數點的數字     |
| `float`（浮點） | `3.14`, `-0.5`    | 有小數點的數字       |
| `str`（字串）   | `"雷姆"`、`'123'` | 用引號包住的文字     |
| `bool`（布林）  | `True`, `False`   | 只有兩種值的邏輯判斷 |

可以透過 type()得知某個變數的類型。

```python
a = 123
b = 3.14
c = "雷姆好可愛"
d = True

print(type(a))  # int
print(type(b))  # float
print(type(c))  # str
print(type(d))  # bool
```

```python
# 文字型的數字 ≠ 數值
x = "123"    # 字串
y = 123      # 整數

print(x + x)  # 結果是 "123123"
print(y + y)  # 結果是 246
```

```python
# NoneType 表示	什麼都沒有、空空的（等於 null）
# 常用在「還沒決定值」的狀況（像剛創角色還沒選職業）
x = None
print(type(x))  # <class 'NoneType'>
```

> [!EXAMPLE] 試著建立以下變數，並用 `type()` 印出資料型態
>
> ```python
> num = 2025
> pi = 3.14159
> name = "艾姬多娜"
> is_cute = True
> nothing = None
> ```

## 5. 輸入資料(input)

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

## 6. 條件句 if/else

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

> [!EXAMPLE] Lab：【猜燈謎遊戲】
> 我們來寫個【猜燈謎遊戲】
> 會有一個題目敘述，玩家可以輸入答案。程式會去比較玩家輸入與答案，並輸出「答對了」或「答錯了」。
>
> ```python
> # Answer
> ans = "圍巾"
> question = "天天跟你黏一起，天冷時才想起。（猜一衣物）"
>
> print(question)
> n = input()
> if n == ans:
>     print("答對了")
> else:
>     print("答錯了")
> ```

> [!EXAMPLE] 角色等級判定器
> 在玩 RPG 遊戲時，如果角色等級超過某個數值，就能進階變職。
> 請你用 if else 幫助教寫一個判斷階級的程式
>
> -   輸入 level(data type 為整數)
> -   如果 level 大於 50，輸出"你是高階冒險者，可以轉職成龍騎士！"
> -   如果 level 小於 50，但大於 30，輸出"你是中階冒險者，可以轉職成劍士！"
> -   如果 level 小於 30，，輸出"你還是初心者，要繼續努力練等喔！"
>
> ```python
> # 玩家等級
> level = int(input("請輸入你的角色等級："))
>
> if level >= 50:
>     print("你是高階冒險者，可以轉職成龍騎士！")
> elif level >= 30:
>     print("你是中階冒險者，可以轉職成劍士！")
> else:
>     print("你還是初心者，要繼續努力練等喔！")
> ```

> [!EXAMPLE] 角色血量警告系統
>
> 幫角色監控血量
>
> -   輸入 hp(data type 為整數)
> -   如果 hp 大於 70，輸出"血量充足，可以上前衝鋒！"
> -   如果 hp 小於 70，但大於 30，輸出"血量中等，請小心行動"！"
> -   如果 hp 小於 30，，輸出"危險！快喝紅水補血！"
>
> ```python
> hp = int(input("請輸入角色目前血量（0-100）："))
>
> if hp >= 70:
>     print("血量充足，可以上前衝鋒！")
> elif hp >= 30:
>     print("血量中等，請小心行動")
> else:
>     print("危險！快喝紅水補血！")
> ```
