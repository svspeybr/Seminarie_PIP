#OEFENING 1: aantal klinkers, medeklinkers en overigez symbolen

def aantalKlinkers(zin):
    KLINKERS = ["a", "e", "i", "o", "u"]
    aantal = 0

    for letter in list(zin):
        if letter.lower() in KLINKERS:
            aantal += 1
    return aantal


def aantalMedeklinkers(zin):
    MEDEKLINKERS = list("bcdfghjklmnpqrstvwxyz")
    aantal = 0

    for letter in list(zin):
        if letter.lower() in MEDEKLINKERS:
            aantal += 1
    return aantal

def overigeSymbolen(zin):
    return len(zin) - aantalKlinkers(zin)- aantalMedeklinkers(zin)


def main():
    zin = input("Vul een zin in: ")
    print("Het aantal klinkers, medeklinkers en overige symbolen zijn resp.:", end =" ")
    print(aantalKlinkers(zin), end =", ")
    print(aantalMedeklinkers(zin), end =" en ")
    print(overigeSymbolen(zin))
    print()

# Run code:
main()

#Oefening 2

def aantalPriem():
    n = int(input("Aantal priemgetallen: "))
    return n

def isPriem(x):
    i = 2
    while (i< x):
        if (x % i == 0):
            return False
        i += 1
    
    return x > 1

def main():
    n = aantalPriem()
    for i in range(n):
        if(isPriem(i)):
            print(i, end = " ")
main()


        