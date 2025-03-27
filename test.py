a_pos = 6 # A的位置
b_pos = 3 # B的位置
all_pos = 30 # 地圖路徑

def f(a, b, all):
    print("起點" + "*" * (a-1) + "A" + "*" * (all-a) + "終點")
    print("起點" + "*" * (b-1) + "B" + "*" * (all-b) + "終點") 

f(a_pos, b_pos, all_pos)