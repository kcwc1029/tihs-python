import tkinter
import tkinter.messagebox # FIXED: 修改程式碼

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
yuka = 0 # FIXED: 計算有幾個塗滿顏色

def main_proc():
    global mx, my, yuka
    if key == "Up" and maze[my-1][mx] == 0:
        my = my - 1
    if key == "Down" and maze[my+1][mx] == 0:
        my = my + 1
    if key == "Left" and maze[my][mx-1] == 0:
        mx = mx - 1
    if key == "Right" and maze[my][mx+1] == 0:
        mx = mx + 1
    if maze[my][mx] == 0:
        maze[my][mx] = 2 # 將貓貓走過的值，由0轉到2=>貓貓就不能走回頭路了
        yuka+=1
        canvas.create_rectangle(mx*80, my*80, mx*80+79, my*80+79, fill="pink", width=0)
    # FIXED: 修改程式碼
    canvas.delete("MYCHR")
    canvas.create_image(mx*80+40, my*80+40, image=img, tag="MYCHR")
    if yuka == 30:
        canvas.update()
        tkinter.messagebox.showinfo("恭喜！", "所有地板都塗色了！")
    else:
        root.after(100, main_proc)


# 建立視窗物件
root = tkinter.Tk()
root.title("顯示迷宮")

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

img = tkinter.PhotoImage(file="mimi_s.png")
canvas.create_image(mx*80+40, my*80+40, image=img, tag="MYCHR")
main_proc()

root.mainloop()


