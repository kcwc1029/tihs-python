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



## 5. 前言

這邊要先給介紹一步動漫【怪獸 8 號】
<span>
<img src="https://i.pinimg.com/736x/9a/02/33/9a0233dc87cc38fa83ad58aca4a61aa5.jpg" width="200px">
<img src="https://i.pinimg.com/474x/93/08/ba/9308ba31c57eaf3de403f20b8d90cd55.jpg" width="200px">
<img src="https://i.pinimg.com/236x/5a/53/8e/5a538e218bb0a25344a73a96d4b20c15.jpg" width="200px">
<img src="https://i.pinimg.com/236x/4e/1c/1c/4e1c1c8487d2aecebadf2e111973f8a0.jpg" width="200px">
</span>

> 主角日比野卡夫卡，任職怪獸清潔公司，做著怪物屍體清潔工的工作。他在小時候跟兒時好友亞白米娜約定「一起消滅所有怪獸」。到現在，米娜已經成為日本防衛隊第 3 部隊的隊長，反觀自己已經放棄加入防衛隊的夢想，過著平庸的生活。
>
> 後來有一天，卡夫卡被一隻神秘的生物侵蝕，將他的身體變成了一隻怪獸 ── 其後被命名為「怪獸 8 號」。卡夫卡變成的怪獸雖然仍然保有人類的意識，但力量跟怪獸無異。他以怪獸之力救了市民之後，看到自己跟米娜並肩作戰的願景，決意加入防衛隊...

卡夫卡，他會需要【召喚/強化】成怪獸 8 號，才可以做出攻擊。
程式也一樣
我們接下來要做的東西，其實是人家寫好的函數庫，那我們要把他【召喚】出來，才能【使用】

## 6. 使用 tkinter 模組

```
import tkinter
```

### 6.1. 顯示視窗

```python
# 引入
import tkinter

# 召喚
root = tkinter.Tk()
# 使用他
root.mainloop()
```

### 6.2. 指定視窗標題與大小

```python
import tkinter # 引入
# 建立視窗
root = tkinter.Tk() # 召喚
root.title("這邊是標題名稱")
root.geometry("400x400")
root.mainloop() # 使用他
```

<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743266637.png" width="80%">
## 2.3. 建立標籤
```python
import tkinter # 引入
# 建立視窗
root = tkinter.Tk() # 召喚
root.title("這邊是標題名稱")
root.geometry("400x400")

# 建立標籤

label = tkinter.Label(root, text="標籤的字串", font=("system", 24))
label.place(x=100, y=100)
root.mainloop() # 使用他

````


![upgit_20250330_1743266998.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743266998.png)

## 2.3. 建立按鈕

```python
import tkinter # 引入

root = tkinter.Tk() # 召喚
root.title("這邊是標題名稱")
root.geometry("400x400")

# 建立標籤
label = tkinter.Label(root, text="標籤的字串", font=("system", 20))
label.place(x=100, y=100)

# 建立按鈕
button = tkinter.Button(root, text="按鈕的字串", font=("system", 20))
button.place(x=100, y=200)

# 顯示
root.mainloop() # 使用他
````

![upgit_20250330_1743267261.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743267261.png)

### 0.1. 為按鈕增加反應

按鈕就是要拿來按的，按完後當然有有反應呀，不然多無趣

```python
import tkinter # 引入

# 按鈕後的事件
def click_btn():
    button["text"] = "OOO我喜歡你"

root = tkinter.Tk() # 召喚
root.title("這邊是標題名稱")
root.geometry("400x400")

# 建立標籤
label = tkinter.Label(root, text="標籤的字串", font=("system", 20))
label.place(x=100, y=100)

# 建立按鈕(增加事件)
button = tkinter.Button(root, text="按鈕的字串", font=("system", 20), command=click_btn)
button.place(x=100, y=200)

# 顯示
root.mainloop() # 使用他
```

## 1. 建立畫布

遊戲中的物件，其實最基礎的方式就是用畫布呈現
![upgit_20250330_1743267687.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743267687.png)

### 1.1. 在畫布(canva)顯示藍色背景

```python
import tkinter # 引入

# 建立視窗
root = tkinter.Tk() # 召喚
root.title("這邊是標題名稱")

# root.geometry("400x400") # 把視窗大小取消掉
# 建立畫布(建立一個前藍色的畫布)
canva = tkinter.Canvas(root, width=200, height=200, bg="skyblue")
canva.pack()

# 顯示
root.mainloop() # 使用他

```

![upgit_20250330_1743267980.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743267980.png)

### 1.2. 在畫布(canva)建立顯示圖片

-   圖片一定要用 png 檔歐
-   [JPG 轉 PNG - 免費線上將 JPG 檔案轉檔成 PNG](https://cdkm.com/tw/jpg-to-png)

```python
import tkinter # 引入

# 建立視窗
root = tkinter.Tk() # 召喚
root.title("這邊是標題名稱")

# 建立畫布(建立一個前藍色的畫布)
canva = tkinter.Canvas(root, width=200, height=200)
canva.pack()
# 載入圖片
img = tkinter.PhotoImage(file="./week03/img.png")
canva.create_image(50, 50, image=img) # 這邊的座標，是圖片的中心點

# 顯示
root.mainloop() # 使用他
```

![upgit_20250330_1743269005.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743269005.png)

## 2. Lab：抽籤遊戲(Draw lots)

不要擔心，助教都會幫你準備好程式碼，接下來你只要盡量嘗試理解就可以了

### 2.1. 建立視窗的背景

-   程式碼：draw_lots01.py
-   不用寫程式，只要開啟檔案，並執行即可

```python
# 程式碼只是給你看看，不用修改任何程式碼！！
import tkinter
# 建立視窗
root = tkinter.Tk()
root.title("抽籤遊戲")
root.resizable(False, False)
# 建立畫布
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="miko.png") # 載入背景圖片
canvas.create_image(400, 300, image=gazou)
root.mainloop()
```

![upgit_20250330_1743270168.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743270168.png)

### 2.2. 配置標籤跟按鈕

-   目標：在原先視窗上，配置標籤與按鈕
-   檔案：draw_lots02.py
    ![upgit_20250330_1743270232.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743270232.png)

```python
# 程式碼只是給你看看，不用修改任何程式碼！！
import tkinter
# 建立視窗
root = tkinter.Tk()
root.title("抽籤遊戲")
root.resizable(False, False)

# 建立畫布
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400, 300, image=gazou)

# 建立標籤
label = tkinter.Label(root, text="？？", font=("Times New Roman", 120), bg="white")
label.place(x=380, y=60)

# 建立按鈕
button = tkinter.Button(root, text="抽籤", font=("Times New Roman", 36), fg="skyblue")
button.place(x=360, y=400)
root.mainloop()
```

### 2.3. 為按鈕增加反應

-   檔案：draw_lots03.py
    ![upgit_20250330_1743270781.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743270781.png)
