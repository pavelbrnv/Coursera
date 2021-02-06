def isPalindrome(number):
    d0 = number % 10
    d1 = (number // 10) % 10
    d2 = (number // 100) % 10
    d3 = (number // 1000) % 10
    return d0 == d3 and d1 == d2


a = int(input())
b = int(input())

if a < b:
    start = a
    end = b
else:
    start = b
    end = a

for i in range(start, end + 1):
    if isPalindrome(i):
        print(i)
