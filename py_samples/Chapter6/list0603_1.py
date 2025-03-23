import tkinter
root = tkinter.Tk()
root.title("第一個按鈕")
root.geometry("800x600")
button = tkinter.Button(root, text="按鈕的字串", font=("Times New Roman", 24))
button.place(x=200, y=100)
root.mainloop()
