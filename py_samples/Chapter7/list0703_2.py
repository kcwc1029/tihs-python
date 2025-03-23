import tkinter
root = tkinter.Tk()
root.title("預設為勾選的狀態")
root.geometry("400x200")
cval = tkinter.BooleanVar()
cval.set(True)
cbtn = tkinter.Checkbutton(text="勾選按鈕", variable=cval)
cbtn.pack()
root.mainloop()
