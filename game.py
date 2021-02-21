import random
import os
import time

print("-------------程序启动-------------")

minimum = int(input("输入答案最小的范围\n"))
maximum = int(input("输入答案最大的范围\n"))

better_maximum = 2 * maximum
print("系统分配的最大范围不应该小于", better_maximum)
maximum = int(input("输入答案最大的范围\n"))

while maximum <= better_maximum:
    print("系统拒绝使用!")
    print("请重新输入!")
    maximum = int(input("输入答案最大的范围\n"))

answer = int(random.randint(minimum, maximum))
quarter_maximum = maximum // 3
better_chance = quarter_maximum - 1
print("可以输入最大的机会是", better_chance)
chance = int(input("输入次数:\n"))

while chance >= quarter_maximum:
    print("系统拒绝使用!")
    chance = int(input("请重新输入:\n"))

now_chance = chance

while now_chance > 0:
    if now_chance == 1:
        print("警告!还剩下最后一次机会!")
    guess = int(input("输入猜想的数字"))
    if guess == answer:
        if now_chance == chance:
            print("一次就过!!!!∑(ﾟДﾟノ)ノ")
        elif now_chance == 1:
            print("你是不是不到一条命就不会玩!")
        print("正确!\n")
        break
    elif guess > answer:
        print("错误!猜想的数字大了.\n")
    else:
        print("错误!猜想的数字小了.\n")
    now_chance = now_chance - 1
    print("剩余次数:", now_chance)

if now_chance == 0:
    print("失败╮(╯﹏╰）╭")
    print("答案是:", answer)
    print("接受惩罚吧!")
    os.system("shutdown -s -t 10")
    time.sleep(5)
    os.system("shutdown -a")
    print("好吧开玩笑的!\n")
print("程序关闭!")
os.system("pause")
