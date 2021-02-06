hh1 = int(input())
mm1 = int(input())
ss1 = int(input())
hh2 = int(input())
mm2 = int(input())
ss2 = int(input())

time1 = hh1 * 3600 + mm1 * 60 + ss1
time2 = hh2 * 3600 + mm2 * 60 + ss2

result = time2 - time1

print(result)
