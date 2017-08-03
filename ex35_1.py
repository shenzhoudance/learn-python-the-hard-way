import random

number = random.randint(1,100)

input_number = input("请输入一个100以内的自然数：")

while number != int(input_number):
    if number > int(input_number):
        print ("小了")
        input_number = input()
    elif number < int(input_number):
        print ("大了")
        input_number = input()

print ("猜对了，这个数是：", number)
