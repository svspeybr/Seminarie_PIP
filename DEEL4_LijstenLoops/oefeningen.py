import random

a= [1,2,3,4,5,4,3,2,1, 0]

#2
for i in range(9):
    a[i]=a[i+1]

#3

total = 0
i = 1
while i < 10:
    total += i
    i+=1

#4 

powerList = []

for i in range(10):
    powerList.append(2**(i+1))

#5

name = input("Enter a word: ")
for i in range(len(name)):
    print(name[len(name)-1-i])

#6
integerList = []
for i in range(20):
    randomInt= random.randrange(0,100)
    integerList.append(randomInt)

print(integerList)

#7 Permutaties

length = 10
pList = []
secList = list(range(1, length +1))
for i in range(length):
    randomPosition = random.randrange(0, len(secList))
    deletedInteger = secList.pop(randomPosition)
    pList.append(deletedInteger)

print(pList)



