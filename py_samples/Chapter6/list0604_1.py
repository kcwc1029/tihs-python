import tkinter
root = tkinter.Tk()
root.title("第一張畫布")
canvas = tkinter.Canvas(root, width=400, height=600, bg="skyblue")
canvas.pack()
root.mainloop()
