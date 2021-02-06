inputs = input().split()

inputsLen = len(inputs)
for i in range(0, inputsLen // 2):
    temp = inputs[i]
    inputs[i] = inputs[inputsLen - i - 1]
    inputs[inputsLen - i - 1] = temp

print(*inputs)
