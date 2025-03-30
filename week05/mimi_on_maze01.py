import tkinter

# FIXED: 新增程式碼
key = ""
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""

# 貓貓起始位置
mx = 1
my = 1

# FIXED: 新增程式碼
def main_proc():
    global mx, my
    if key == "Up" and maze[my-1][mx] == 0:
        my = my - 1
    if key == "Down" and maze[my+1][mx] == 0:
        my = my + 1
    if key == "Left" and maze[my][mx-1] == 0:
        mx = mx - 1
    if key == "Right" and maze[my][mx+1] == 0:
        mx = mx + 1
    canvas.coords("MYCHR", mx*80+40, my*80+40)
    root.after(100, main_proc)




# 建立視窗物件
root = tkinter.Tk()
root.title("顯示迷宮")

# FIXED: 新增程式碼
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

# 建立畫布
canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.pack()

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
    ]

# 使用雙層迴圈走訪迷宮資料
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            # 畫出灰色方塊，位置為 (x*80, y*80)，每格是 80x80 大小
            canvas.create_rectangle(x*80, y*80, x*80+80, y*80+80, fill="gray")

# FIXED: 新增程式碼
img = tkinter.PhotoImage(file="mimi_s.png")
canvas.create_image(mx*80+40, my*80+40, image=img, tag="MYCHR")
main_proc()

root.mainloop()

