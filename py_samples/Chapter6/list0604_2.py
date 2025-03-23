import tkinter
root = tkinter.Tk()
root.title("第一次顯示圖片")
canvas = tkinter.Canvas(root, width=400, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="iroha.png")
canvas.create_image(200, 300, image=gazou)
root.mainloop()
