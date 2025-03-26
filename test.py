##### 函數：輸出 #####
def while_print(num):
    i = 0
    while i<num:
        print(f"{i} 拉姆好可愛")
        i+=1
    print()

##### 相加 #####
def cute(a, b):
    c = a + b
    return c
    
##### 主程式 #####
temp = cute(1, 1)
ans = cute(temp, temp)
while_print(ans)

# 0 拉姆好可愛
# 1 拉姆好可愛
# 2 拉姆好可愛
# 3 拉姆好可愛