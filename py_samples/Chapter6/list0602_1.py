import tkinter
root = tkinter.Tk()
root.title("第一個標籤")
root.geometry("800x600")
label = tkinter.Label(root, text="標籤的字串", font=("System", 24))
label.place(x=200, y=100)
root.mainloop()
