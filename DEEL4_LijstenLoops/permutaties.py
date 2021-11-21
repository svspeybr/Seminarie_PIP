import random

pList = []
secList = list(range(1,11))

for i in range(10):
    integer = secList.pop(random.randrange(0, len(secList)))
    pList.append(integer)

print(pList)