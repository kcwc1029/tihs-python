import tkinter
key = 0
def key_down(e):
    global key
    key = e.keycode
    print("KEY:"+str(key))

root = tkinter.Tk()
root.title("取得鍵碼")
root.bind("<KeyPress>", key_down)
root.mainloop()
