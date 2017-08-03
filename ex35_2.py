import random

number = random.randint(1,100)

for i in range(0,100):
    input_number = input("请输入一个100以内的自然数：")
    if number > int(input_number):
        print ("小了")
    elif number < int(input_number):
        print ("大了")
    else:
        print ("猜对了，这个数是：", number)
        break
