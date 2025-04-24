## 1. 前景提要

我們上一次學了：
- 了解python是什麼
- 安裝python的環境：thonny
- 資料型態：int、float、char、string、bool
- 輸出：print
- 輸入：input
	- 預設是字串（string），如果要轉成整數int

很建議同學利用課後時間，把這邊的講義文件，看著自己敲敲看，這真的挺重要的


## 2. 輸出字串月曆

阿!!!!，這時助教想起來，助教這個月好像要跟雷姆一起去看電影，但忘記是哪一天了(ಠ 益 ಠ)
小朋友，你可以幫我看一下這個月的時間嗎？

<img src="https://i.pinimg.com/236x/b3/6b/95/b36b9501aecb662cb3cc6a4fb6421635.jpg" width="300px">

因此，我們現在需要【月曆模組】我們要如何載入他呢

-   在 thonny 中安裝模組
-   在程式碼中說 我要載入【月曆模組】

> [!NOTE] 補充：檔案(模組 module)的載入方式
> 東西不是一次載入進來，而是【需要甚麼，才載入甚麼】

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



## 3. 條件句 if/else

這是助教在【Re:從零開始的異世界生活】最喜歡的三個角色(阿還有愛姬多那)

因為助教平時在研究室敲鍵盤敲得好痛苦，想買個手伴，讓冷冷的桌面有一點溫興的感覺。
但是，助教因為手頭緊緊，確定無法 3 個手伴都買，那這時候，就是一個人生交叉十字路口的選擇...

<span>
<img src="https://i.pinimg.com/736x/91/cd/da/91cdda3fe434aacfda3c784d1ce108ab.jpg" width="45%">
<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250323_1742722899.png" width="45%">
</span>

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



### 3.1. Lab：練習猜燈謎

當用戶輸入指令後，我們需要告知機器，要依據用戶的輸入，去做判斷
假設我們做了一道謎題：「天天跟你黏一起，天冷時才想起。（猜一衣物）」（答案是圍巾）
那我們想要讓玩家輸入答案，並告訴玩家是否正確

```python
ans = "圍巾"
question = "天天跟你黏一起，天冷時才想起。（猜一衣物）"

n = input(question)
if ans == question:
    print("答對了")
else:
    print("答錯了")
```

### 3.2. Lab：角色等級判斷

在玩 RPG 遊戲時，如果角色等級超過某個數值，就能進階變職。請你用 if else 幫助教寫一個判斷階級的程式。

-   輸入 level(data type 為整數)
-   如果 level 大於 50，輸出"你是高階冒險者，可以轉職成龍騎士！"
-   如果 level 小於 50，但大於 30，輸出"你是中階冒險者，可以轉職成劍士！"
-   如果 level 小於 30，，輸出"你還是初心者，要繼續努力練等喔！"

```python
# 玩家等級
level = int(input("請輸入你的角色等級："))

if ...
	print("你是高階冒險者，可以轉職成龍騎士！")
elif ...
	print("你是中階冒險者，可以轉職成劍士！")
else:
	print("你還是初心者，要繼續努力練等喔！")
```


### 3.3. Lab：臭直男感情判斷器

```python
message = input("臭直男感情判斷器\n請輸入對方訊息：")

if message == "我們可以談談嗎？" or message == "你最近變了" or message == "我覺得我們不適合":
    print("⚠️ 警告：有分手風險！")
else:
    print("💗 放心啦，感情穩定")
```









