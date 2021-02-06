inputs = input().split()
k, c = input().split()
index = int(k)

inputs.append('dummy')
for i in range(len(inputs) - 1, index, -1):
    inputs[i] = inputs[i - 1]
inputs[index] = c

print(*inputs)
