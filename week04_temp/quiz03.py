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
