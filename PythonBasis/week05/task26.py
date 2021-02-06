inputs = input().split()
index = int(input())

for i in range(index + 1, len(inputs)):
    inputs[i - 1] = inputs[i]
inputs.pop()

print(*inputs)
