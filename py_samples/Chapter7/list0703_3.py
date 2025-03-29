import tkinter

def check():
    if cval.get() == True:
        print("已勾選")
    else:
        print("未勾選")

root = tkinter.Tk()
root.title("取得勾選狀態")
root.geometry("400x200")


cval = tkinter.BooleanVar()
cval.set(False)
cbtn = tkinter.Checkbutton(text="勾選按鈕", variable=cval, command=check)
cbtn.pack()
root.mainloop()
