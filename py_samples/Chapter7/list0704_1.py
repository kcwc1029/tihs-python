import tkinter
import tkinter.messagebox

def click_btn():
    tkinter.messagebox.showinfo("資訊", "點選按鈕了")

root = tkinter.Tk()
root.title("第一個訊息方塊")
root.geometry("400x200")
btn = tkinter.Button(text="測試", command=click_btn)
btn.pack()
root.mainloop()
