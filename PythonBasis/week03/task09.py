x = 1
xSqSum = 0
xSum = 0
counter = 0

while x != 0:
    x = int(input())
    if x != 0:
        xSqSum += x * x
        xSum += x
        counter += 1

m = xSum / counter

d = xSqSum - (2 * m * xSum) + (m * m * counter)
sigma = (d / (counter - 1)) ** 0.5

print(sigma)
