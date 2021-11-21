###RECURSIE

##VB1
def printDriehoek(hoogte):
    if hoogte < 1: return
    else:
        print("[]" * hoogte)
        printDriehoek(hoogte - 1)

##VB2

def printDriehoek(hoogte):
    if hoogte < 1: return
    else:
        printDriehoek(hoogte - 1)
        print("[]" * hoogte)
        