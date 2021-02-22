values1 = set(map(int, input().split()))
values2 = set(map(int, input().split()))
crossing_ordered_values = sorted(values1 & values2)
print(*crossing_ordered_values)
