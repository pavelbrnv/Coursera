n = int(input())
normal = n % (3600 * 24)

ss = normal % 60
mm = (normal // 60) % 60
hh = normal // 3600

ssStr = str(ss)
mmStr = str(mm)
hhStr = str(hh)

ssPrefix = '0' * (2 - len(ssStr))
mmPrefix = '0' * (2 - len(mmStr))

print(hhStr, mmPrefix + mmStr, ssPrefix + ssStr, sep=':', end='')
