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
- 剪刀、石頭、布
- 像助教是邊緣可達鴨，沒人跟我玩(哭)

<img src="https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250326_1742983287.png" width="300px">

```python
import random 

r = random.randint(1,6) # 產出借於1-6之間得整數
print(r) 
```

## 2. CUI與GUI

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


其實電腦的本身是屬於CUI(character user interface，字元使用者介面)（像是python的shell），就是透過文字與指令來操控電腦。
但這樣是不是看起來很可怕，也很不近人情，因此工程師就在寫一個圖形介面程序，將CUI轉成GUI(Graphical User Interface)。這有兩個影響點
- 使用上更加親民
- 效率會比較差(因為中間多了一到手續)

![upgit_20250326_1742985952.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2025/03/upgit_20250326_1742985952.png)


也因此，我們所看到的遊戲，他就是在GUI下面的產物。

<span>
<img src="https://i.pinimg.com/736x/d4/5e/f4/d45ef4f4e7eb8201124d3343fffc5aaa.jpg" height="300px">
<img src="https://i.pinimg.com/736x/b4/ba/ca/b4baca019140e1c8ce6cf5cdb7b7890e.jpg" height="300px">
</span>

阿，但但但，這樣的一個遊戲，其實已經不單單是只有程式了，還有遊戲美術，企劃等等。
若我們只想聚焦於程式這一塊的話，也是可以，但就是，做出來不會到那麼好看。
所以，我們會聚焦在遊戲的一個邏輯，並用CUI的方式去完成。
## 3. Lab：抽卡包

<img src="https://down-tw.img.susercontent.com/file/tw-11134207-7rasm-m1smlgx827t7b4@resize_w450_nl.webp" height="300px">

假設SSR抽取機率為1%，意旨「抽100次只會有1次的機會會中」。或許有些人的理解是「那我只要抽100次，就一定會中」。那~是這樣嗎？
所謂的1%，還是會有人抽一次就中(歐皇)，還是會有人抽200-300次還是不中。
接著，就讓我們來實作看看這種機制：

> 我們稍微改一下
> 將機率訂為10%，就是「抽10次只會有1次的機會會中」之機率。

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
> - 增加遊戲的 緊張感與挑戰性
> - 防止玩家「輕易逃脫 → 無敵解法」
> - 符合戰鬥策略設計（有風險就會更刺激）
> 
> 假設遊戲設定為【如果玩家選擇撤退，失敗機率要33%(1/3)】
> 我們可以先隨機產生一個數字(介於1-100)
> 如果數值在30以內(<30) => 撤退失敗
> 反之(30-70) => 撤退成功
> 
> 【資料補充】[【專欄】論述「JRPG」在戰鬥系統上的「變」與「不變」 - 巴哈姆特](https://gnn.gamer.com.tw/detail.php?sn=161035)


## 4. Lab：大富翁

大富翁是邊丟骰子一邊往前的遊戲，如果我們要用CUI的方式去表現的話。
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
