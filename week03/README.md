## 1. 前言

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

## 2. 使用 tkinter 模組

```
import tkinter
```

### 2.1. 顯示視窗

```python
# 引入
import tkinter

# 召喚
root = tkinter.Tk()
# 使用他
root.mainloop()
```

### 2.2. 指定視窗標題與大小

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
