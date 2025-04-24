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
