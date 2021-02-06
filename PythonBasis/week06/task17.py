distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

distances.sort(reverse=True)
prices.sort()

total_price = 0
for i in range(len(distances)):
    personal_price = distances[i] * prices[i]
    total_price += personal_price

print(total_price)
