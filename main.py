import tkinter
import random
import time
import _thread
import sys
# 画面作成
version = tkinter.Tcl().eval('info patchlevel')
root = tkinter.Tk()
canvas = tkinter.Canvas(width=1920, height=1080, bg="white")
canvas.pack()
root.title("TETORIS")
key = ""
mino1 = 0
mino2 = 0
mino3 = 0
mino4 = 0
count1 = 0
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""
def mino_down():
    global maps, putting
    maps[mino1[0]][mino1[1]] = 0
    maps[mino2[0]][mino2[1]] = 0
    maps[mino3[0]][mino3[1]] = 0
    maps[mino4[0]][mino4[1]] = 0
    serch_y = 1
    if maps[mino1[0]][mino1[1] + serch_y] == 0 and maps[mino2[0]][mino2[1] + serch_y] == 0 and maps[mino3[0]][mino3[1] + serch_y] == 0 and maps[mino4[0]][mino4[1] + serch_y] == 0:
        serch_y += 1
    else:
        putting = 1
    mino1[1] = mino1[1] + serch_y - 1
    mino2[1] = mino2[1] + serch_y - 1
    mino3[1] = mino3[1] + serch_y - 1
    mino4[1] = mino4[1] + serch_y - 1
    maps[mino1[0]][mino1[1]] = mino[i]
    maps[mino2[0]][mino2[1]] = mino[i]
    maps[mino3[0]][mino3[1]] = mino[i]
    maps[mino4[0]][mino4[1]] = mino[i]
def put():
    global putting
    time.sleep(0.1)
    putting = 0
def byouga():
    global maps, count1
    try:
        canvas.delete("block")
        erase()
        for x in range(12):
            for y in range(20):
                base_x = 640 - ookisa * 6 + x*ookisa
                if maps[x][y] == 9:
                    canvas.create_rectangle(base_x, y*ookisa, base_x + ookisa, y*ookisa + ookisa, fill="black", tag="block")
                if maps[x][y] == 0:
                    canvas.create_rectangle(base_x, y*ookisa, base_x + ookisa, y*ookisa + ookisa, fill="gray", tag="block")
                if maps[x][y] == 1:
                    canvas.create_rectangle(base_x, y*ookisa, base_x + ookisa, y*ookisa + ookisa, fill="skyblue", tag="block")
                if maps[x][y] == 2:
                    canvas.create_rectangle(base_x, y*ookisa, base_x + ookisa, y*ookisa + ookisa, fill="yellow", tag="block")
                if maps[x][y] == 3:
                    canvas.create_rectangle(base_x, y*ookisa, base_x + ookisa, y*ookisa + ookisa, fill="green", tag="block")
                if maps[x][y] == 4:
                    canvas.create_rectangle(base_x, y*ookisa, base_x + ookisa, y*ookisa + ookisa, fill="red", tag="block")
                if maps[x][y] == 5:
                    canvas.create_rectangle(base_x, y*ookisa, base_x + ookisa, y*ookisa + ookisa, fill="blue", tag="block")
                if maps[x][y] == 6:
                    canvas.create_rectangle(base_x, y*ookisa, base_x + ookisa, y*ookisa + ookisa, fill="orange", tag="block")
                if maps[x][y] == 7:
                    canvas.create_rectangle(base_x, y*ookisa, base_x + ookisa, y*ookisa + ookisa, fill="purple", tag="block")
        canvas.update()
        count1 += 1
    except:
        print("Error!")
        sys.exit()
def i_mino():
    global mino1, mino2, mino3, mino4, maps
    mino = 1
    mino1 = [4, 1]
    mino2 = [5, 1]
    mino3 = [6, 1]
    mino4 = [7, 1]
    maps[4][1] = mino
    maps[5][1] = mino
    maps[6][1] = mino
    maps[7][1] = mino
def o_mino():
    global mino1, mino2, mino3, mino4, maps
    mino = 2
    mino1 = [5, 1]
    mino2 = [5, 2]
    mino3 = [6, 1]
    mino4 = [6, 2]
    maps[5][1] = mino
    maps[5][2] = mino
    maps[6][1] = mino
    maps[6][2] = mino
def s_mino():
    global mino1, mino2, mino3, mino4, maps
    mino = 3
    mino1 = [5, 1]
    mino2 = [5, 2]
    mino3 = [4, 2]
    mino4 = [6, 1]
    maps[5][1] = mino
    maps[5][2] = mino
    maps[4][2] = mino
    maps[6][1] = mino
def z_mino():
    global mino1, mino2, mino3, mino4, maps
    mino = 4
    mino1 = [5, 1]
    mino2 = [5, 2]
    mino3 = [4, 1]
    mino4 = [6, 2]
    maps[5][1] = mino
    maps[5][2] = mino
    maps[4][1] = mino
    maps[6][2] = mino
def j_mino():
    global mino1, mino2, mino3, mino4, maps
    mino = 5
    mino1 = [6, 2]
    mino2 = [5, 2]
    mino3 = [4, 2]
    mino4 = [4, 1]
    maps[6][2] = mino
    maps[5][2] = mino
    maps[4][2] = mino
    maps[4][1] = mino
def l_mino():
    global mino1, mino2, mino3, mino4, maps
    mino = 6
    mino1 = [6, 2]
    mino2 = [5, 2]
    mino3 = [4, 2]
    mino4 = [6, 1]
    maps[6][2] = mino
    maps[5][2] = mino
    maps[4][2] = mino
    maps[6][1] = mino
def t_mino():
    global mino1, mino2, mino3, mino4, maps
    mino = 7
    mino1 = [5, 1]
    mino2 = [5, 2]
    mino3 = [4, 2]
    mino4 = [6, 2]
    maps[5][1] = mino
    maps[5][2] = mino
    maps[4][2] = mino
    maps[6][2] = mino
def nanimosinai():
    aaa = 0
def erase():
    global maps, putting
    tates = []
    if putting == 1:
        for i in range(len(maps[0])):
            tate = []
            for j in range(len(maps)):
                tate.append(maps[j][i])
            tates.append(tate)
        for i in reversed(range(len(tates))):
            if (not 0 in tates[i]) and tates[i][5] != 9:
                tates[i] = [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]
                tates.pop(i)
                tates.insert(1, [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9])
        maps = []
        for i in range(len(tates[0])):
            map1 = []
            for j in range(len(tates)):
                map1.append(tates[j][i])
            maps.append(map1)
ookisa = 40
maps = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9 ,9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9 ,9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
]
game_over = 0
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
putting = 0
while True:
    if game_over == 1:
        break
    serch_y = 0
    serch_x = 0
    mino = [1, 2, 3, 4, 5, 6, 7]
    random.shuffle(mino)
    mino[0] = 1
    for i in range(7):
        root.after(20, byouga())
        putting = 0
        stop = 0
        if game_over == 1:
            break
        if mino[i] == 1:
            i_mino()
        if mino[i] == 2:
            o_mino()
        if mino[i] == 3:
            s_mino()
        if mino[i] == 4:
            z_mino()
        if mino[i] == 5:
            j_mino()
        if mino[i] == 6:
            l_mino()
        if mino[i] == 7:
            t_mino()
        time.sleep(0.02)
        t_down = time.time()
        putting = 0
        while True:
            if time.time() - t_down > 1:
                t_down = time.time()
                mino_down()
            if putting == 1:
                break
            if game_over == 1:
                break
            while key == "Up":
                root.after(20, byouga())
            fps1 = time.time()
            root.after(20, byouga())
            if key == "Up":
                maps[mino1[0]][mino1[1]] = 0
                maps[mino2[0]][mino2[1]] = 0
                maps[mino3[0]][mino3[1]] = 0
                maps[mino4[0]][mino4[1]] = 0
                serch_y = 0
                while True:
                    if maps[mino1[0]][mino1[1] + serch_y] == 0 and maps[mino2[0]][mino2[1] + serch_y] == 0 and maps[mino3[0]][mino3[1] + serch_y] == 0 and maps[mino4[0]][mino4[1] + serch_y] == 0:
                        serch_y += 1
                    else:
                        break
                mino1[1] = mino1[1] + serch_y - 1
                mino2[1] = mino2[1] + serch_y - 1
                mino3[1] = mino3[1] + serch_y - 1
                mino4[1] = mino4[1] + serch_y - 1
                maps[mino1[0]][mino1[1]] = mino[i]
                maps[mino2[0]][mino2[1]] = mino[i]
                maps[mino3[0]][mino3[1]] = mino[i]
                maps[mino4[0]][mino4[1]] = mino[i]
                putting = 1
                break
            if key == "Down":
                maps[mino1[0]][mino1[1]] = 0
                maps[mino2[0]][mino2[1]] = 0
                maps[mino3[0]][mino3[1]] = 0
                maps[mino4[0]][mino4[1]] = 0
                maps[mino1[0]][mino1[1]] = 0
                maps[mino2[0]][mino2[1]] = 0
                maps[mino3[0]][mino3[1]] = 0
                maps[mino4[0]][mino4[1]] = 0
                serch_y = 1
                if maps[mino1[0]][mino1[1] + serch_y] == 0 and maps[mino2[0]][mino2[1] + serch_y] == 0 and maps[mino3[0]][mino3[1] + serch_y] == 0 and maps[mino4[0]][mino4[1] + serch_y] == 0:
                    serch_y += 1
                else:
                    putting = 1
                mino1[1] = mino1[1] + serch_y - 1
                mino2[1] = mino2[1] + serch_y - 1
                mino3[1] = mino3[1] + serch_y - 1
                mino4[1] = mino4[1] + serch_y - 1
                maps[mino1[0]][mino1[1]] = mino[i]
                maps[mino2[0]][mino2[1]] = mino[i]
                maps[mino3[0]][mino3[1]] = mino[i]
                maps[mino4[0]][mino4[1]] = mino[i]
            if key == "Right":
                serch_x = 1
                maps[mino1[0]][mino1[1]] = 0
                maps[mino2[0]][mino2[1]] = 0
                maps[mino3[0]][mino3[1]] = 0
                maps[mino4[0]][mino4[1]] = 0
                if maps[mino1[0] + serch_x][mino1[1]] == 0 and maps[mino2[0] + serch_x][mino2[1]] == 0 and maps[mino3[0] + serch_x][mino3[1]] == 0 and maps[mino4[0] + serch_x][mino4[1]] == 0:
                    serch_x = 1
                else:
                    serch_x = 0
                mino1[0] = mino1[0] + serch_x
                mino2[0] = mino2[0] + serch_x
                mino3[0] = mino3[0] + serch_x
                mino4[0] = mino4[0] + serch_x
                maps[mino1[0]][mino1[1]] = mino[i]
                maps[mino2[0]][mino2[1]] = mino[i]
                maps[mino3[0]][mino3[1]] = mino[i]
                maps[mino4[0]][mino4[1]] = mino[i]
            if key == "Left":
                serch_x = -1
                maps[mino1[0]][mino1[1]] = 0
                maps[mino2[0]][mino2[1]] = 0
                maps[mino3[0]][mino3[1]] = 0
                maps[mino4[0]][mino4[1]] = 0
                if maps[mino1[0] + serch_x][mino1[1]] == 0 and maps[mino2[0] + serch_x][mino2[1]] == 0 and maps[mino3[0] + serch_x][mino3[1]] == 0 and maps[mino4[0] + serch_x][mino4[1]] == 0:
                    serch_x = -1
                else:
                    serch_x = 0
                mino1[0] = mino1[0] + serch_x
                mino2[0] = mino2[0] + serch_x
                mino3[0] = mino3[0] + serch_x
                mino4[0] = mino4[0] + serch_x
                maps[mino1[0]][mino1[1]] = mino[i]
                maps[mino2[0]][mino2[1]] = mino[i]
                maps[mino3[0]][mino3[1]] = mino[i]
                maps[mino4[0]][mino4[1]] = mino[i]
        if mino1[1] < 2 or mino2[1] < 2 or mino3[1] < 2 or mino4[1] < 2:
            game_over = 1
byouga()
print("game over")