## 1. 建立輸入欄位
文字輸入欄位可以分為：
- 單列輸入Entry
- 多列輸入Text

### 1.1. 單列輸入Entry

```python
import tkinter

# 建立視窗
root = tkinter.Tk()
root.title("這是視窗名稱")
root.geometry("400x200")

# 建立欄位
entry = tkinter.Entry(width=20)
entry.place(x=10, y=10)
root.mainloop()
```

![upgit_20250330_1743271443.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743271443.png)


### 1.2. 操作Entry的字串
Entry的字串可以透過get()取得
我們來試試【按下按鈕後，輸出文字，並把按鈕上的文字也改掉】

```python
import tkinter
def click_btn():
    txt = entry.get() # 取的字串
    print(txt)
    button["text"] = txt


# 建立視窗
root = tkinter.Tk()
root.title("這是視窗名稱")
root.geometry("400x200")

# 建立欄位
entry = tkinter.Entry(width=20)
entry.place(x=10, y=10)

# 建立按鈕
button = tkinter.Button(text="取得字串", command=click_btn)
button.place(x=20, y=100)
root.mainloop()
```

### 1.3. 多列輸入Text
我們來試試在多行欄位中，連續輸入文字。

```python
import tkinter
def click_btn():
    text.insert(tkinter.END, "孩子該上課搂！\n")

# 建立視窗
root = tkinter.Tk()
root.title("這是視窗名稱")
root.geometry("400x200")

# 建立按鈕
button = tkinter.Button(text="訊息", command=click_btn)
button.pack()

# 建立文字物件
text = tkinter.Text()
text.pack()
root.mainloop()
```

## 2. 建立勾選按鈕(checkbutton)
```python
import tkinter

# 建立視窗
root = tkinter.Tk()
root.title("這是視窗名稱")
root.geometry("400x200")

# 建立勾選按鈕
cbtn = tkinter.Checkbutton(text="勾選按鈕")
cbtn.pack()
root.mainloop()
```
### 2.1. 一開始決定勾選狀態
```python
import tkinter

# 建立視窗
root = tkinter.Tk()
root.title("這是視窗名稱")
root.geometry("400x200")

# 建立勾選按鈕
cval = tkinter.BooleanVar() # 勾選按鈕的狀態
cval.set(True)
cbtn = tkinter.Checkbutton(text="勾選按鈕", variable=cval)
cbtn.pack()
root.mainloop()
```


### 2.2. 取得勾選狀態

```python
import tkinter

def check():
    if cval.get() == True:
        print("已勾選")
    else:
        print("未勾選")


# 建立視窗
root = tkinter.Tk()
root.title("這是視窗名稱")
root.geometry("400x200")

# 建立勾選按鈕
cval = tkinter.BooleanVar() # 勾選按鈕的狀態
cval.set(False)
cbtn = tkinter.Checkbutton(text="勾選按鈕", variable=cval, command=check)
cbtn.pack()
root.mainloop()
```

## 3. 彈出訊息視窗
要利用tkinter.messagebox模組
- showinfo()：顯示 資訊訊息（一般提示）
- showwarning()：顯示 警告訊息（例如提醒用戶）
- showerror()：顯示 錯誤訊息（例如發生錯誤）
- askyesno()	：顯示「是 / 否」按鈕，回傳 True 或 False
- askokcancel()：顯示「確定 / 取消」按鈕，回傳 True 或 False

```python
import tkinter
import tkinter.messagebox

# 彈出視窗按鈕
def click_btn():
    tkinter.messagebox.showinfo("資訊", "點選按鈕了")


# 建立視窗
root = tkinter.Tk()
root.title("這是視窗名稱")
root.geometry("400x200")

# 建立按鈕
btn = tkinter.Button(text="測試", command=click_btn)
btn.pack()
root.mainloop()
```

![upgit_20250330_1743272367.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743272367.png)

## 4. Lab：詢問遊戲(Quiz)

### 4.1. 建立視窗的背景
-   程式碼：quiz01.py
-   不用寫程式，只要開啟檔案，並執行即可

```python
# 程式碼只是給你看看，不用修改任何程式碼！！
import tkinter
# 建立視窗
root = tkinter.Tk()
root.title("你是哪種類型的貓貓~~~")
root.resizable(False, False)
# 建立畫布
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="sumire.png") # 載入圖片
canvas.create_image(400, 300, image=gazou)
# 載入按鈕
button = tkinter.Button(text="診斷", font=("Times New Roman", 32), bg="lightgreen")
button.place(x=400, y=480)
# 載入文字
text = tkinter.Text(width=40, height=5, font=("Times New Roman", 16))
text.place(x=320, y=30)
root.mainloop()
```
![upgit_20250330_1743272906.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743272906.png)

### 4.2. 配置勾選按鈕
你在視窗上看的勾選框，其實是分為
-   程式碼：quiz02.py
-   不用寫程式，只要開啟檔案，並執行即可

```python
import tkinter
# 建立視窗
root = tkinter.Tk()
root.title("你是哪種類型的貓貓~~~")
root.resizable(False, False)
# 建立畫布
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="sumire.png") # 載入圖片
canvas.create_image(400, 300, image=gazou)
# 載入按鈕
button = tkinter.Button(text="診斷", font=("Times New Roman", 32), bg="lightgreen")
button.place(x=400, y=480)
# 載入文字
text = tkinter.Text(width=40, height=5, font=("Times New Roman", 16))
text.place(x=320, y=30)

# FIXED: 增加下面程式碼
items = [
    "喜歡高處，覺得地板不配我踩",
    "聽到塑膠袋聲音會瞬間衝刺",
    "貓貓最愛盒子！",
    "碰到罐頭聲音，衝得比Wi-Fi還快",
    "對味道很敏感",
    "對雷射筆有復仇情結",
    "晚上不睡覺，凌晨三點上演《跑酷人生》	"
]

# 儲存每個勾選狀態
check_vars = []

for i, item in enumerate(items):
    var = tkinter.BooleanVar()
    chk = tkinter.Checkbutton(text=item, font=("Times New Roman", 12), variable=var, bg="#dfe")
    chk.place(x=400, y=160 + i * 40)
    check_vars.append(var)
    
root.mainloop()
```

![upgit_20250330_1743274263.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743274263.png)


### 4.3. 增加按鈕反應
-   程式碼：quiz03.py
-   不用寫程式，只要開啟檔案，並執行即可

```python
import tkinter

# FIXED: 增加下面程式碼
def click_btn():
    # 計算有幾個 True（有勾選）
    score = sum(var.get() for var in check_vars)  
    result = f"你總共勾選了 {score} 項行為喵！"
    
    # 清除舊內容，插入新內容
    text.delete("1.0", tkinter.END) # 刪除文字(從第1行第0個字，到最後)
    text.insert(tkinter.END, result) # 再把最新的文字插入到文字框

# 建立視窗
root = tkinter.Tk()
root.title("你是哪種類型的貓貓~~~")
root.resizable(False, False)
# 建立畫布
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="sumire.png") # 載入圖片
canvas.create_image(400, 300, image=gazou)
# 載入按鈕
button = tkinter.Button(text="診斷", font=("Times New Roman", 32), bg="lightgreen", command=click_btn) # FIXED: 修改這裡
button.place(x=400, y=480)
# 載入文字
text = tkinter.Text(width=40, height=5, font=("Times New Roman", 16))
text.place(x=320, y=30)

items = [
    "喜歡高處，覺得地板不配我踩",
    "聽到塑膠袋聲音會瞬間衝刺",
    "貓貓最愛盒子！",
    "碰到罐頭聲音，衝得比Wi-Fi還快",
    "對味道很敏感",
    "對雷射筆有復仇情結",
    "晚上不睡覺，凌晨三點上演《跑酷人生》	"
]

# 儲存每個勾選狀態
check_vars = []

for i, item in enumerate(items):
    var = tkinter.BooleanVar()
    chk = tkinter.Checkbutton(text=item, font=("Times New Roman", 12), variable=var, bg="#dfe")
    chk.place(x=400, y=160 + i * 40)
    check_vars.append(var)
    
root.mainloop()
```
![upgit_20250330_1743274088.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743274088.png)

### 4.4. 依據不同數量給出評語
```python
import tkinter

# FIXED: 增加下面程式碼
def click_btn():
    # 計算有幾個 True（有勾選）
    score = sum(var.get() for var in check_vars)  
    result = ""
    if score == 0:
        result = "你連貓的呼嚕聲都不會模仿，這輩子離貓最接近的時刻可能是看貓貓迷因。"
    elif score == 1 or score == 2:
        result = "你只是個普普通通的人類，但可能偷偷追蹤了幾個貓咪IG帳號。"
    elif score == 3:
        result = "你有一點貓味（？）可能半夜會突然想跳到桌上。"
    elif score == 4:
        result = "你開始懷疑自己是不是貓變的… 有時候真的不想理人。"
    elif score == 5:
        result = "你根本就是貓星人在人類社會的臥底，喵一聲來聽聽！"
    elif score == 6:
        result = "前世八成是隻有貓德的貓，連路邊浪浪都想跟你打招呼。"
    else:
        result = "外表看起來是人，但骨子裡就是隻精緻的、傲嬌的、凌晨三點狂奔的主子喵！"

    # 清除舊內容，插入新內容
    text.delete("1.0", tkinter.END) # 刪除文字(從第1行第0個字，到最後)
    text.insert(tkinter.END, result) # 再把最新的文字插入到文字框

# 建立視窗
root = tkinter.Tk()
root.title("你是哪種類型的貓貓~~~")
root.resizable(False, False)
# 建立畫布
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="sumire.png") # 載入圖片
canvas.create_image(400, 300, image=gazou)
# 載入按鈕
button = tkinter.Button(text="診斷", font=("Times New Roman", 32), bg="lightgreen", command=click_btn) # FIXED: 修改這裡
button.place(x=400, y=480)
# 載入文字
text = tkinter.Text(width=40, height=5, font=("Times New Roman", 16))
text.place(x=320, y=30)

items = [
    "喜歡高處，覺得地板不配我踩",
    "聽到塑膠袋聲音會瞬間衝刺",
    "貓貓最愛盒子！",
    "碰到罐頭聲音，衝得比Wi-Fi還快",
    "對味道很敏感",
    "對雷射筆有復仇情結",
    "晚上不睡覺，凌晨三點上演《跑酷人生》	"
]

# 儲存每個勾選狀態
check_vars = []

for i, item in enumerate(items):
    var = tkinter.BooleanVar()
    chk = tkinter.Checkbutton(text=item, font=("Times New Roman", 12), variable=var, bg="#dfe")
    chk.place(x=400, y=160 + i * 40)
    check_vars.append(var)
    
root.mainloop()
```

![upgit_20250330_1743274717.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743274717.png)

## 5. 即時處理？
遊戲在執行中，會不斷進行多項處理，不管玩家有沒有操作。
系統會根據「時間順序」持續執行相關功能。
常見的即時處理內：
- 敵人會在畫面上持續移動
- 背景動畫(像雲飄動、水面搖晃，背景也會不停變化)
- 如果是限時遊戲，計時器會持續倒數
- 玩家不操作時處理：即使玩家沒有動作，遊戲仍在持續進行處理

### 5.1. 使用after()
```python
import tkinter
# 執行程式，每秒遞增並顯示
time = 0
def count_up():
    global time
    tmr = tmr + 1
    label["text"] = tmr
    root.after(1000, count_up) # 經過一秒，執行count_up()

# 建立視窗
root = tkinter.Tk()
# 建立標籤
label = tkinter.Label(font=("Times New Roman", 80))
label.pack()

root.after(1000, count_up) # 經過一秒，執行count_up()
root.mainloop()
```
### 5.2. 全域變數&區域變數

![upgit_20250330_1743275197.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743275197.png)

![upgit_20250330_1743275737.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743275737.png)

![upgit_20250330_1743275819.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250330_1743275819.png)







