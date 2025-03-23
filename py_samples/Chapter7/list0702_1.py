import tkinter

def click_btn():
    text.insert(tkinter.END, "怪物出現了！")

root = tkinter.Tk()
root.title("輸入多列文字")
root.geometry("400x200")
button = tkinter.Button(text="訊息", command=click_btn)
button.pack()
text = tkinter.Text()
text.pack()
root.mainloop()
