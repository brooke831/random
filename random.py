import random

start = int(input("請輸入起始值:"))
end = int(input("請輸入結束值:"))
 
r = random.randint(start , end )
count = 0
while True:
    count += 1
    num = int(input("請猜猜看隨機數字:"))
    if num == r :
        print("猜中")
        break
    elif num > r:
        print("請猜比答案小")
    elif num < r :
        print("請猜比答案大" )
    print("這是你猜的第", count, "次")