import tkinter

# 建立視窗物件
root = tkinter.Tk()
root.title("顯示迷宮")

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

root.mainloop()
