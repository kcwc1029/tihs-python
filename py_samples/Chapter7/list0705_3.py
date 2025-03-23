import tkinter

def click_btn():
    pts = 0
    for i in range(7):
        if bvar[i].get() == True:
            pts = pts + 1
    text.delete("1.0", tkinter.END)
    text.insert("1.0", "勾選的個數是" + str(pts))

root = tkinter.Tk()
root.title("貓咪相似度診斷程式")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="sumire.png")
canvas.create_image(400, 300, image=gazou)
button = tkinter.Button(text="診斷", font=("Times New Roman", 32), bg="lightgreen", command=click_btn)
button.place(x=400, y=480)
text = tkinter.Text(width=40, height=5, font=("Times New Roman", 16))
text.place(x=320, y=30)

bvar = [None]*7
cbtn = [None]*7
ITEM = [
"喜歡高處",
"看到球就想玩",
"嚇一跳的時候，頭髮會立起來",
"喜歡造型像老鼠的玩具",
"對味道很敏感",
"喜歡啃魚骨",
"晚上特別有精神"
]
for i in range(7):
    bvar[i] = tkinter.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=("Times New Roman", 12), variable=bvar[i], bg="#dfe")
    cbtn[i].place(x=400, y=160+40*i)
root.mainloop()
