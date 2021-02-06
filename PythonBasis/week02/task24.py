l1 = int(input())
w1 = int(input())
h1 = int(input())

l2 = int(input())
w2 = int(input())
h2 = int(input())

lc = int(input())
wc = int(input())
hc = int(input())

hMax = h1
if h2 > hMax:
    hMax = h2

hFull = h1 + h2

tl1 = l1 + l2
tw1 = w1
if w2 > tw1:
    tw1 = w2
c1 = ((tl1 <= lc and tw1 <= wc) or (tl1 <= wc and tw1 <= lc)) and hMax <= hc

tl2 = l1 + w2
tw2 = w1
if l2 > tw2:
    tw2 = l2
c2 = ((tl2 <= lc and tw2 <= wc) or (tl2 <= wc and tw2 <= lc)) and hMax <= hc

tl3 = l1
if l2 > tl3:
    tl3 = l2
tw3 = w1 + w2
c3 = ((tl3 <= lc and tw3 <= wc) or (tl3 <= wc and tw3 <= lc)) and hMax <= hc

tl4 = l1
if w2 > tl4:
    tl4 = w2
tw4 = w1 + l2
c4 = ((tl4 <= lc and tw4 <= wc) or (tl4 <= wc and tw4 <= lc)) and hMax <= hc

ol1 = l1
if l2 > ol1:
    ol1 = l2
ow1 = w1
if w2 > ow1:
    ow1 = w2
c5 = ((ol1 <= lc and ow1 <= wc) or (ol1 <= wc and ow1 <= lc)) and hFull <= hc

ol2 = l1
if w2 > ol2:
    ol2 = w2
ow2 = w1
if l2 > ow2:
    ow2 = l2
c6 = ((ol2 <= lc and ow2 <= wc) or (ol2 <= wc and ow2 <= lc)) and hFull <= hc

if c1 or c2 or c3 or c4 or c5 or c6:
    print('YES')
else:
    print('NO')
