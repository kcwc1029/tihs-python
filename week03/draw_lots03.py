import tkinter
import random # FIXED
# 建立視窗
root = tkinter.Tk()
root.title("抽籤遊戲")
root.resizable(False, False)

# FIXED: 增加函數反應
def click_btn():
    label["text"]=random.choice(["大吉", "中吉", "小吉", " 凶 "])
    label.update()

# 建立畫布
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400, 300, image=gazou)

# 建立標籤
label = tkinter.Label(root, text="？？", font=("Times New Roman", 120), bg="white")
label.place(x=380, y=60)

# 建立按鈕
button = tkinter.Button(root, text="抽籤", font=("Times New Roman", 36), fg="skyblue", command=click_btn) # FIXED
button.place(x=360, y=400)
root.mainloop()
