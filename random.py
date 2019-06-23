import random 
r = random.randint(1,100)
count = 0
while True:
    count += 1
    num = int(input("請輸入號碼:"))
    if num == r :
        print("猜中")
        break
    elif num > r:
        print("比答案大")
    elif num < r :
        print("比答案小" )
    print("這是你猜的第", count, "次")