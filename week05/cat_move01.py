import tkinter

# 用來儲存目前按下的按鍵名稱（例如 "Up", "Left" 等）
key = ""

# 當按下鍵盤時呼叫，將 key 記下來
def key_down(e):
    global key
    key = e.keysym

# 當放開鍵盤時呼叫，將 key 清空
def key_up(e):
    global key
    key = ""


# 主角的初始位置（x, y）
cx = 400
cy = 300

# 每 0.1 秒執行一次的主要邏輯
def main_proc():
    global cx, cy
    if key == "Up":
        cy = cy - 20
    if key == "Down":
        cy = cy + 20
    if key == "Left":
        cx = cx - 20
    if key == "Right":
        cx = cx + 20
    canvas.coords("MYCHR", cx, cy) # 將圖片移動到新位置（使用標籤 "MYCHR" 找到
    root.after(100, main_proc)

# 建立主視窗
root = tkinter.Tk()
root.title("移動角色")

# 視窗綁定事件
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

# 建立畫布
canvas = tkinter.Canvas(width=800, height=600, bg="lightgreen")
canvas.pack()

# 建立圖片
img = tkinter.PhotoImage(file="mimi.png")
canvas.create_image(cx, cy, image=img, tag="MYCHR")

main_proc()
root.mainloop()
