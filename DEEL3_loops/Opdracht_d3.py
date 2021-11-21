import random

woord = input("Voer een woord in: ")
n = 1
while n <= len(woord):
    i = random.randrange(0, len(woord)-1)
    j = random.randrange(i+1, len(woord))
    n += 1

    begin = woord[0:i]
    midden = woord[i+1:j]
    einde = woord[j+1:]

    woord = begin + woord[j] + midden + woord[i] + einde

print(woord)
    