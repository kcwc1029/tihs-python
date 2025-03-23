import tkinter

def click_btn():
    button["text"] = "點選按鈕了"

root = tkinter.Tk()
root.title("第一個按鈕")
root.geometry("800x600")
button = tkinter.Button(root, text="請點選按鈕", font=("Times New Roman", 24), command=click_btn)
button.place(x=200, y=100)
root.mainloop()
