values1 = set(map(int, input().split()))
values2 = set(map(int, input().split()))
crossing_values = values1 & values2
print(len(crossing_values))
