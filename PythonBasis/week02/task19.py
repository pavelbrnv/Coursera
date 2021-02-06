storeX = int(input())
storeY = int(input())
storeZ = int(input())
boxX = int(input())
boxY = int(input())
boxZ = int(input())

caseA = (storeX // boxX) * (storeY // boxY) * (storeZ // boxZ)
caseB = (storeX // boxY) * (storeY // boxX) * (storeZ // boxZ)
caseC = (storeX // boxX) * (storeY // boxZ) * (storeZ // boxY)
caseD = (storeX // boxY) * (storeY // boxZ) * (storeZ // boxX)
caseE = (storeX // boxZ) * (storeY // boxX) * (storeZ // boxY)
caseF = (storeX // boxZ) * (storeY // boxY) * (storeZ // boxX)

caseMax = caseA
if caseB > caseMax:
    caseMax = caseB
if caseC > caseMax:
    caseMax = caseC
if caseD > caseMax:
    caseMax = caseD
if caseE > caseMax:
    caseMax = caseE
if caseF > caseMax:
    caseMax = caseF

print(caseMax)
