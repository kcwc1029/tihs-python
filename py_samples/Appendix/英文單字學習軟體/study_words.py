import tkinter

FNT1 = ("Times New Roman", 12)
FNT2 = ("Times New Roman", 24)

WORDS = [
"apple", "蘋果",
"book", "書",
"cat", "貓",
"dog", "狗",
"egg", "雞蛋",
"fire", "火焰",
"gold", "金色",
"head", "頭",
"ice", "冰",
"juice", "果汁",
"king", "國王",
"lemon", "檸檬",
"mother", "媽媽",
"notebook", "筆記本",
"orange", "橘子",
"pen", "筆",
"queen", "女王",
"room", "房間",
"sport", "體育",
"time", "時間",
"user", "使用者",
"vet", "獸醫",
"window", "窗戶",
"xanadu", "桃花源",
"yellow", "黃色",
"zoo", "動物園"
]
MAX = int(len(WORDS)/2)
score = 0
word_num = 0
yourword = ""
koff = False #讓玩家一個字一個字輸入答案的旗標

def key_down(e):
    global score, word_num, yourword, koff
    if koff == True:
        koff = False
        kcode = e.keycode
        ksym  = e.keysym
        if 65 <= kcode and kcode <= 90: #大寫英文字母
            yourword = yourword + chr(kcode+32)
        if 97 <= kcode and kcode <= 122: #小寫英文字母
            yourword = yourword + chr(kcode)
        if ksym == "Delete" or ksym == "BackSpace":
            yourword = yourword[:-1] # 利用這行程式刪掉尾巴的1個字母
        input_label["text"] = yourword
        if ksym == "Return":
            if input_label["text"] == english_label["text"]:
                score = score + 1
                set_label()

def key_up(e):
    global koff
    koff = True

def set_label():
    global word_num, yourword
    score_label["text"] = score
    english_label["text"] = WORDS[word_num*2]
    japanese_label["text"] = WORDS[word_num*2+1]
    input_label["text"] = ""
    word_num = (word_num + 1)%MAX
    yourword = ""

root = tkinter.Tk()
root.title("單字學習軟體")
root.geometry("400x200")
root.resizable(False, False)
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
root["bg"] = "#DEF"

score_label = tkinter.Label(font=FNT1, bg="#DEF", fg="#4C0")
score_label.pack()
english_label = tkinter.Label(font=FNT2, bg="#DEF")
english_label.pack()
japanese_label = tkinter.Label(font=FNT1, bg="#DEF", fg="#444")
japanese_label.pack()
input_label = tkinter.Label(font=FNT2, bg="#DEF")
input_label.pack()
howto_label = tkinter.Label(text="輸入英文單字後按下[Enter]鍵\n重新輸入按下[Delete]或[BS]", font=FNT1, bg="#FFF", fg="#ABC")
howto_label.pack()

set_label()
root.mainloop()
