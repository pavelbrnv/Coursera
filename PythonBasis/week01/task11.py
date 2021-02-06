n = int(input())
normalN = n % 1440
hours = normalN // 60
minutes = normalN % 60
print(hours, minutes)
