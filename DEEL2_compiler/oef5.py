# oef 5 - deel 2
# Vraag twee getallen op (werk met variabelen a, b )
a = float(input("Geef een getal:"))
b = float(input("Geef een tweede getal:"))

#vergelijk het verschil
if abs(a - b ) < 10 ** (-2):
    print("De getallen zijn gelijk tot op twee decimalen nauwkeurig.")
else:
    print("De getallen zijn verschillend.")

