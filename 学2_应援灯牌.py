# -*- coding:utf-8 -*-
"""
应援灯牌
========
先从键盘读入灯牌几排、每排几盏。
领队站在第 2 排、从左数第 3 盏。这一盏打印 ×，其余打印 ●。
再按排数打三角：第 1 排 1 盏，第 2 排 2 盏。每一排收进列表，用 len 打印一共几排。

灯牌墙打完后，电池还剩 20。还够亮一整排，就再亮一轮，用掉这一排的盏数。
一开始不知道能亮几轮，用 while。不够一整排就停。

先输入 3 和 5，应看到灯牌墙、三排三角，以及：

    第 1 轮亮完，电池还剩 15
    第 2 轮亮完，电池还剩 10
    第 3 轮亮完，电池还剩 5
    第 4 轮亮完，电池还剩 0
    一共亮了 4 轮

再输入 4 和 6。第二排是 ●●×●●●。三角一共 4 排。电池亮 3 轮，还剩 2。

两组都要打对。

要求：
1. 排数和每排盏数都转成整数。
2. 灯牌墙：外层管第几排，内层管每一盏。领队那一盏打 ×。
3. 三角也是两层循环。第 r 排打 r 盏，收进列表后再打印。排数用 len。
4. 电池从 20 开始。while 的条件是电池还够这一排的盏数。每一轮轮数加 1，电池减去盏数。
5. 在 PyCharm 里运行。先输入 3 和 5，再输入 4 和 6。
"""
# TODO ① 读入排数和每排盏数，打灯牌墙
rows =int(input("行数："))
cols = int(input("列数："))
for row in range(1,rows+1):
    for col in range(1, cols+1):
        if row ==2 and col ==3:

           print("×", end="")
        else:
            print("●", end="")
    print()

for row in range(1,rows+1 ):
    for col in range(row):
        print("●", end="")


    print()
print("三角一共", rows, "排")



battery=20
rounds=0
while battery>=cols:
    rounds+=1
    battery-=cols
    print("第",rounds,"轮亮完，电池还剩",battery)
print("一共亮了",rounds,"轮")
# TODO ② 打三角，收进列表，用 len 打印一共几排


# TODO ③ 电池 20，while 还够一排就再亮一轮
