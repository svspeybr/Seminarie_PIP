
### VB A
#functie definiëren

def cubeVolume(sideLength):
    volume = sideLength ** 3
    return volume

## functie uitvoeren
#vb1
print(cubeVolume(4))
#vb2
for i in range(2,8):
    print(cubeVolume(i), end =" ")
print()

 ### VB B
#functie definiëren

def sayHello():
    print("Hello!")

#functie uitvoeren
sayHello()

### VB C
#functie definiëren 
def splitWith(symb, word):
    splittedWord = ""
    for letter in list(word):
        splittedWord += letter + symb

    return splittedWord[: len(splittedWord)-1]

# functie uitvoeren
print(splitWith("+", "hallo"))
