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
