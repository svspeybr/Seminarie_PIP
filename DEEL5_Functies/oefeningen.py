#1 Beschouw de functies

import math

def f(x):
    return g(x) + math.sqrt(h(x))

def g(x):
    return 4 * h(x)

def h(x):
    return x*x + k(x) - 1

def k(x):
    return 2 *(x + 1)

# Bepaal
##A
print("f(2)=",f(2))
##B
print("g(h(2))=",g(h(2)))
##C
print("k(g(2)+h(2))=",k(g(2)+h(2)))

#2 

def splitWith(symb, word):
    splittedWord = ""
    for letter in list(word):
        splittedWord += letter + symb

    return splittedWord[: len(splittedWord)-1]

print(splitWith("+", splitWith("+", "Hola")))

#3 Vermoeden van Collatz

def collatz(n):
    while n > 1:
        print(n, end= " ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print()
    return n 

##
print("Collatz for n = 1:", end = " ")
collatz(1)
print("Collatz for n = 2:", end = " ")
collatz(2)
print("Collatz for n = 10:", end = " ")
collatz(10)

# 4 
def abs(getal):
    if getal < 0:
        getal = getal *(-1)
    return getal

# 5
def cilinderVol(r, h):
    return math.pi * (r ** 2) *h 

def cilinderOpp(r, h):
    mantelOpp = 2 * math.pi * r * h
    grondVlakOpp =  math.pi *(r ** 2)
    return mantelOpp + 2 * grondVlakOpp

#6
def maximum(a, b, c):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c

    return max

#test 
print("max van -5, 56, 2.3:", maximum(-5, 56, 2.3))

#7 
def telWoorden(string):
    stringLijst = list(string)
    aantal = 1
    for teken in stringLijst:
        if teken == " ":
            aantal += 1
    return aantal

print("Aantal woorden versie 1:", telWoorden("Marie heeft een goudvis"))
### EXTRA 1: De functie telWoorden is niet ideaal:
# vind voorbeelden van strings waarvoor telWoorden meer woorden aangeeft dan er zijn.

### (***) We kunnen telWoorden() als volgt verbeteren:
# gebruik een variabele 'eindeWoord' (einde van een woord == gebied na het woord met enkel spaties) zodat...
# - als eindeWoord == True:
#       'aantal' woorden ENKEL toeneemt van zodra een niet-spatie teken gevonden wordt (dus een nieuw woord)
# - als eindeWoord == False: (een woord wordt doorlopen)
#        zet eindeWoord = True van zodra een spatie gevonden is op het einde van het woord.

def telWoorden2(string):
    stringLijst = list(string)
    aantal = 0
    eindeWoord = True
    for teken in stringLijst:
        if eindeWoord:
            if teken != " ": # eerste letter van nieuw woord gevonden
                aantal += 1
                eindeWoord = False # Zet op False: nieuw woord gevonden
        elif teken == " ": #einde van het woord gevonden
            eindeWoord = True
    return aantal

print("Aantal woorden versie 2:", telWoorden2("  Marie heeft  een enorme inktvis  "))