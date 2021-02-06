a = int(input())
b = int(input())
n = int(input())
price = (a * 100) + b
totalPrice = price * n
print(totalPrice // 100, totalPrice % 100)
