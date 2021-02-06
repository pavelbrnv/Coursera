l1 = int(input())
r1 = int(input())

l2 = int(input())
r2 = int(input())

l3 = int(input())
r3 = int(input())

# crossing
c12 = l2 <= r1 and l1 <= r2
c13 = l3 <= r1 and l1 <= r3
c23 = l3 <= r2 and l2 <= r3

# move 1 to 2-3
ml1 = r2
if r3 < ml1:
    ml1 = r3
mr1 = ml1 + (r1 - l1)
cm12 = l2 <= mr1 and ml1 <= r2
cm13 = l3 <= mr1 and ml1 <= r3

# move 2 to 1-3
ml2 = r1
if r3 < ml2:
    ml2 = r3
mr2 = ml2 + (r2 - l2)
c1m2 = ml2 <= r1 and l1 <= mr2
cm23 = l3 <= mr2 and ml2 <= r3

# move 3 to 1-2
ml3 = r1
if r2 < ml3:
    ml3 = r2
mr3 = ml3 + (r3 - l3)
c1m3 = ml3 <= r1 and l1 <= mr3
c2m3 = ml3 <= r2 and l2 <= mr3

if (c12 and c13) or (c12 and c23) or (c13 and c23):
    print(0)
elif (cm12 and cm13) or (cm12 and c23) or (cm13 and c23):
    print(1)
elif (c1m2 and c13) or (c1m2 and cm23) or (c13 and cm23):
    print(2)
elif (c12 and c1m3) or (c12 and c2m3) or (c1m3 and c2m3):
    print(3)
else:
    print(-1)
