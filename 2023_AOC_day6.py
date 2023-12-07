import math

inp = '''Time:        44     80     65     72
Distance:   208   1581   1050   1102'''

'''
L = inp.split()

Races = []
n = len(L) // 2
for i in range(1, n):
    tup = (int(L[i]), int(L[i + n]))
    Races.append(tup)

total = 1
for tup in Races:
    # (x * (tup[0] - x)) > tup[0]
    count = 0
    for x in range(tup[0]):
        if (x * (tup[0] - x)) > tup[1]:
            print(tup[0], x)
            count += 1
    total *= count
print(total)'''

L = inp.split()

n = len(L) // 2
t = ""
d = ""
for i in range(1, n):
    t += L[i]
    d += L[i + n]

tup = (int(t), int(d))

count = 0
for x in range(tup[0]):
    if (x * (tup[0] - x)) > tup[1]:
        count += 1

print(count)