import tkinter
root = tkinter.Tk()
root.title("第一個文字輸入欄位")
root.geometry("400x200")
entry = tkinter.Entry(width=20)
entry.place(x=10, y=10)
root.mainloop()
