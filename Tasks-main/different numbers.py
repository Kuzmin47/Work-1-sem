number = int(input())
units = number % 100 % 10
dozens = number // 10 % 10
hundreds = number // 100
if (units != dozens and dozens != hundreds and hundreds != units):
    print(1)
else:
    print(0)