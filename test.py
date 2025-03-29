import tkinter
# 執行程式，每秒遞增並顯示
time = 0
def count_up():
    time += 1
    label["text"] = time
    root.after(1000, count_up) # 經過一秒，執行count_up()

# 建立視窗
root = tkinter.Tk()
# 建立標籤
label = tkinter.Label(font=("Times New Roman", 80))
label.pack()

root.after(1000, count_up) # 經過一秒，執行count_up()
root.mainloop()