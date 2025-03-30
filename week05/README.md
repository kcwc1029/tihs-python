## 1. 事件

【事件】：使用者(user)對鍵盤滑鼠操作的行為
	e.g.藉由滑鼠，點擊視窗裡的圖片，即為【對圖片觸發了點擊事件】

python可利用bind()接收事件
```python
# bind()語法
bind("事件", 要觸發的函數)
```

### 1.1. 鍵盤與滑鼠事件綁定對照

| 事件名稱                         | 觸發時機    | 補充說明                                |
| ---------------------------- | ------- | ----------------------------------- |
| `<KeyPress>` 或 `<Key>`       | 按下鍵盤時   | 可用於偵測按鍵編號或字符（`e.keycode`, `e.char`） |
| `<KeyRelease>`               | 放開鍵盤按鍵時 | 可以搭配做連發控制或判斷何時鬆開鍵                   |
| `<Motion>`                   | 滑鼠移動時   | 可用於滑鼠追蹤、畫圖、遊戲照準器等                   |
| `<ButtonPress>` 或 `<Button>` | 點擊滑鼠按鍵時 | 預設為左鍵，右鍵需額外指定（例如 `<Button-3>`）      |
|                              |         |                                     |


### 1.2. 嘗試利用bind()取得按鍵編號

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
> 請你藉由程式碼，幫我查詢以下案件的keyCode


| 方向鍵左 | 方向鍵右 | 方向鍵上 | 方向鍵下 | Enter | A   | Z   | 0   | 9   |
| ---- | ---- | ---- | ---- | ----- | --- | --- | --- | --- |
|      |      |      |      |       |     |     |     |     |

### 1.3. 輸入按鈕，將keycode填入標籤

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


### 1.4. 從ketcode去判斷方向鍵
接下來我們要延伸，再取得keycode後，去對應出方向鍵
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
<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743320145.png" width="50%">
</div>


![upgit_20250330_1743320657.png|672x365](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743320657.png)
