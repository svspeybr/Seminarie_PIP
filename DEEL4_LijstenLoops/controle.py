#1
names = ["Fritz"]
names.insert(1, "Ann")
names.insert(0, "Sue")
names.pop(2)
names.append("Lee")

#2 
FirstName = names[0] #onthoud de eerste naam
names[0] = names[len(names)-1] #overschrijf de eerste naam
names[len(names)-1] = FirstName

#3
scores = [2,5, 7, 10]
print(sum(scores)//len(scores))

#4 
a = [2, 1, 2, 1]
b = [2, 1]
print(a + b == b + a)
print(a == b)