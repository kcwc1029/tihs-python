## 1. 事件

【事件】：使用者(user)對鍵盤滑鼠操作的行為
e.g.藉由滑鼠，點擊視窗裡的圖片，即為【對圖片觸發了點擊事件】

python 可利用 bind()接收事件

```python
# bind()語法
bind("事件", 要觸發的函數)
```

### 1.1. 鍵盤與滑鼠事件綁定對照

| 事件名稱                      | 觸發時機       | 補充說明                                          |
| ----------------------------- | -------------- | ------------------------------------------------- |
| `<KeyPress>` 或 `<Key>`       | 按下鍵盤時     | 可用於偵測按鍵編號或字符（`e.keycode`, `e.char`） |
| `<KeyRelease>`                | 放開鍵盤按鍵時 | 可以搭配做連發控制或判斷何時鬆開鍵                |
| `<Motion>`                    | 滑鼠移動時     | 可用於滑鼠追蹤、畫圖、遊戲照準器等                |
| `<ButtonPress>` 或 `<Button>` | 點擊滑鼠按鍵時 | 預設為左鍵，右鍵需額外指定（例如 `<Button-3>`）   |
|                               |                |                                                   |

### 1.2. 嘗試利用 bind()取得按鍵編號

```python
import tkinter

key = 0

def key_down(e):  # 加上 e 接收事件物件
    global key
    key = e.keycode  # 取得按鍵的代碼
    print(f"key: {key}")

root = tkinter.Tk()
root.title("取得按鍵號碼")
root.bind("<KeyPress>", key_down)  # 綁定鍵盤按下事件

root.mainloop()
```

> [!EXAMPLE] Lab
> 請你藉由程式碼，幫我查詢以下案件的 keyCode

| 方向鍵左 | 方向鍵右 | 方向鍵上 | 方向鍵下 | Enter | A   | Z   | 0   | 9   |
| -------- | -------- | -------- | -------- | ----- | --- | --- | --- | --- |
|          |          |          |          |       |     |     |     |     |

### 1.3. 輸入按鈕，將 keycode 填入標籤

```python
import tkinter

key = 0
# 按下按鍵所觸發的事件
def key_down(e):
    global key
    key = e.keycode

# 修改標籤
def main_proc():
    label["text"] = key
    root.after(100, main_proc)

# 建立視窗
root = tkinter.Tk()
root.title("即時按鍵輸入處理")
root.bind("<KeyPress>", key_down) # 綁定
# 建立標籤
label = tkinter.Label(font=("Times New Roman", 80))
label.pack()
main_proc()

root.mainloop()
```

### 1.4. 從 ketcode 去判斷方向鍵

接下來我們要延伸，再取得 keycode 後，去對應出方向鍵

```python
import tkinter

key = 0
# 按下按鍵所觸發的事件
def key_down(e):
    global key
    # key = e.keycode
    key = e.keysym # FIXED：修改這裡

# 修改標籤
def main_proc():
    label["text"] = key
    root.after(100, main_proc)

# 建立視窗
root = tkinter.Tk()
root.title("即時按鍵輸入處理")
root.bind("<KeyPress>", key_down) # 綁定
# 建立標籤
label = tkinter.Label(font=("Times New Roman", 80))
label.pack()
main_proc()

root.mainloop()
```

## 2. Lab：控制貓貓移動

-   程式碼：cat_move01.py
-   不用寫程式，只要開啟檔案，並執行即可

![upgit_20250330_1743316478.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743316478.png)

```python
# 程式碼只是給你看看，不用修改任何程式碼！！
import tkinter

# 用來儲存目前按下的按鍵名稱（例如 "Up", "Left" 等）
key = ""

# 當按下鍵盤時呼叫，將 key 記下來
def key_down(e):
    global key
    key = e.keysym

# 當放開鍵盤時呼叫，將 key 清空
def key_up(e):
    global key
    key = ""


# 主角的初始位置（x, y）
cx = 400
cy = 300

# 每 0.1 秒執行一次的主要邏輯
def main_proc():
    global cx, cy
    if key == "Up":
        cy = cy - 20
    if key == "Down":
        cy = cy + 20
    if key == "Left":
        cx = cx - 20
    if key == "Right":
        cx = cx + 20
    canvas.coords("MYCHR", cx, cy) # 將圖片移動到新位置（使用標籤 "MYCHR" 找到
    root.after(100, main_proc)

# 建立主視窗
root = tkinter.Tk()
root.title("移動角色")

# 視窗綁定事件
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

# 建立畫布
canvas = tkinter.Canvas(width=800, height=600, bg="lightgreen")
canvas.pack()

# 建立圖片
img = tkinter.PhotoImage(file="mimi.png")
canvas.create_image(cx, cy, image=img, tag="MYCHR")

main_proc()
root.mainloop()
```

## 3. 二維陣列

![upgit_20250330_1743318681.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743318681.png)

可以想像成一張表格，像是 Excel，有「行（row）」和「列（column）」

```python
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

取值

```python
print(m[0][1])  # 2，第一列的第二個元素
print(m[2][0])  # 7，第三列的第一個元素
```

修改陣列中的值

```python
m[1][1] = 999  # 把中間那格改成 999
```

走訪整個二維陣列

```python
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for y in range(len(m)):          # 走訪每一列（行）
    for x in range(len(m[y])):   # 走訪該列中的每一格
        print(f"m[{y}][{x}] = {m[y][x]}")
```

晉賢

> [!EXAMPLE] Lab
> 題目
> 應該要輸出甚麼

> [!EXAMPLE] Lab
> 題目
> 應該要輸出甚麼

### 3.1. 以二維陣列定義迷宮

<div align="center">
<span >
<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743319421.png" width="400px">
<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743319571.png" width="400px">
</span>
</div>

<div align="center">
<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743319735.png" width="50%">
</div>

```python
import tkinter

# 建立視窗物件
root = tkinter.Tk()
root.title("顯示迷宮")

# 建立畫布
canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.pack()

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
    ]

# 使用雙層迴圈走訪迷宮資料
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            # 畫出灰色方塊，位置為 (x*80, y*80)，每格是 80x80 大小
            canvas.create_rectangle(x*80, y*80, x*80+80, y*80+80, fill="gray")

root.mainloop()
```

<div align="center">
<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743320145.png" width="40%">
<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743321041.png" width="40%">
</div>

### 3.2. 將貓貓放入迷宮，並開始移動

![upgit_20250330_1743322579.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743322579.png)

接下來要讓貓咪在我們的迷宮之中晃晃

-   程式碼：mimi_on_maze01.py
-   不用寫程式，只要開啟檔案，並執行即可

```python
# 程式碼只是給你看看，不用修改任何程式碼！！
import tkinter

# FIXED: 新增程式碼
key = ""
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""

# 貓貓起始位置
mx = 1
my = 1

# FIXED: 新增程式碼
def main_proc():
    global mx, my
    if key == "Up" and maze[my-1][mx] == 0:
        my = my - 1
    if key == "Down" and maze[my+1][mx] == 0:
        my = my + 1
    if key == "Left" and maze[my][mx-1] == 0:
        mx = mx - 1
    if key == "Right" and maze[my][mx+1] == 0:
        mx = mx + 1
    canvas.coords("MYCHR", mx*80+40, my*80+40)
    root.after(100, main_proc)




# 建立視窗物件
root = tkinter.Tk()
root.title("顯示迷宮")

# FIXED: 新增程式碼
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

# 建立畫布
canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.pack()

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
    ]

# 使用雙層迴圈走訪迷宮資料
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            # 畫出灰色方塊，位置為 (x*80, y*80)，每格是 80x80 大小
            canvas.create_rectangle(x*80, y*80, x*80+80, y*80+80, fill="gray")

# FIXED: 新增程式碼
img = tkinter.PhotoImage(file="mimi_s.png")
canvas.create_image(mx*80+40, my*80+40, image=img, tag="MYCHR")
main_proc()

root.mainloop()
```

![upgit_20250330_1743321395.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743321395.png)

### 3.3. 幫貓貓增加路徑

接下來要讓貓咪在我們的迷宮之中晃晃

-   程式碼：mimi_on_maze02.py
-   不用寫程式，只要開啟檔案，並執行即可

```python
# 程式碼只是給你看看，不用修改任何程式碼！！
import tkinter

key = ""
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""

# 貓貓起始位置
mx = 1
my = 1

def main_proc():
    global mx, my
    if key == "Up" and maze[my-1][mx] == 0:
        my = my - 1
    if key == "Down" and maze[my+1][mx] == 0:
        my = my + 1
    if key == "Left" and maze[my][mx-1] == 0:
        mx = mx - 1
    if key == "Right" and maze[my][mx+1] == 0:
        mx = mx + 1

    # FIXED: 修改程式碼
    if maze[my][mx] == 0:
        maze[my][mx] = 2 # 將貓貓走過的值，由0轉到2=>貓貓就不能走回頭路了
        canvas.create_rectangle(mx*80, my*80, mx*80+79, my*80+79, fill="pink", width=0)
    canvas.delete("MYCHR")
    canvas.create_image(mx*80+40, my*80+40, image=img, tag="MYCHR")
    root.after(100, main_proc)

# 建立視窗物件
root = tkinter.Tk()
root.title("顯示迷宮")

root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

# 建立畫布
canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.pack()

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
    ]

# 使用雙層迴圈走訪迷宮資料
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            # 畫出灰色方塊，位置為 (x*80, y*80)，每格是 80x80 大小
            canvas.create_rectangle(x*80, y*80, x*80+80, y*80+80, fill="gray")

img = tkinter.PhotoImage(file="mimi_s.png")
canvas.create_image(mx*80+40, my*80+40, image=img, tag="MYCHR")
main_proc()

root.mainloop()
```

![upgit_20250330_1743322051.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743322051.png)

### 3.4. 判斷是否過過關

接下來要讓貓咪在我們的迷宮之中晃晃

-   程式碼：mimi_on_maze03.py
-   不用寫程式，只要開啟檔案，並執行即可

```python
# 程式碼只是給你看看，不用修改任何程式碼！！
import tkinter
import tkinter.messagebox # FIXED: 修改程式碼

key = ""
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""

# 貓貓起始位置
mx = 1
my = 1
yuka = 0 # FIXED: 計算有幾個塗滿顏色

def main_proc():
    global mx, my, yuka
    if key == "Up" and maze[my-1][mx] == 0:
        my = my - 1
    if key == "Down" and maze[my+1][mx] == 0:
        my = my + 1
    if key == "Left" and maze[my][mx-1] == 0:
        mx = mx - 1
    if key == "Right" and maze[my][mx+1] == 0:
        mx = mx + 1
    if maze[my][mx] == 0:
        maze[my][mx] = 2 # 將貓貓走過的值，由0轉到2=>貓貓就不能走回頭路了
        yuka+=1
        canvas.create_rectangle(mx*80, my*80, mx*80+79, my*80+79, fill="pink", width=0)
    # FIXED: 修改程式碼
    canvas.delete("MYCHR")
    canvas.create_image(mx*80+40, my*80+40, image=img, tag="MYCHR")
    if yuka == 30:
        canvas.update()
        tkinter.messagebox.showinfo("恭喜！", "所有地板都塗色了！")
    else:
        root.after(100, main_proc)


# 建立視窗物件
root = tkinter.Tk()
root.title("顯示迷宮")

root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

# 建立畫布
canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.pack()

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
    ]

# 使用雙層迴圈走訪迷宮資料
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            # 畫出灰色方塊，位置為 (x*80, y*80)，每格是 80x80 大小
            canvas.create_rectangle(x*80, y*80, x*80+80, y*80+80, fill="gray")

img = tkinter.PhotoImage(file="mimi_s.png")
canvas.create_image(mx*80+40, my*80+40, image=img, tag="MYCHR")
main_proc()

root.mainloop()
```

![upgit_20250330_1743322497.png|806x593](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743322497.png)

> [!NOTE] 如何完成遊戲軟體
> 很多人雖然會寫程式，但一說到「要自己做一個遊戲」，腦袋就空了 🤯
> 這很正常！一開始我學寫程式時也是這樣。
>
> 做遊戲，其實就是把很多「小處理」一段一段組起來，就像煮一道菜一樣——你要準備材料、切切切、炒一炒、調味、最後才端出來。
> 遊戲的開發也是這樣，一步步把要做的功能完成，最後才會變成完整的作品。
>
> ![upgit_20250330_1743323124.png|642x411](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743323124.png)
>
> 要完成一個簡單的遊戲，其實要包含
> 🕹️ 鍵盤輸入
> ⏱️ 即時處理（定時更新）
> 🧱 二維陣列代表迷宮地圖
> 🎯 控制角色的位置
> 🎨 畫出迷宮格子 這些都是「做遊戲的基礎能力」，就像蓋房子前先準備鋼筋水泥。

> [!NOTE] 那要如何開始寫一個遊戲？
>
> -   先想像遊戲完成後長什麼樣（有什麼畫面？角色能幹嘛？）
> -   列出你會需要什麼功能（角色移動、判斷迷宮格子、變顏色、勝利條件...）
> -   把每個功能拆開來，一個一個做
> -   每完成一小段，你就離完成更近了！💪
