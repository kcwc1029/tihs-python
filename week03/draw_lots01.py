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
