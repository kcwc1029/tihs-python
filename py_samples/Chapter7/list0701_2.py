import tkinter

def click_btn():
    txt = entry.get()
    button["text"] = txt

root = tkinter.Tk()
root.title("第一個文字輸入欄位")
root.geometry("400x200")
entry = tkinter.Entry(width=20)
entry.place(x=20, y=20)
button = tkinter.Button(text="取得字串", command=click_btn)
button.place(x=20, y=100)
root.mainloop()
