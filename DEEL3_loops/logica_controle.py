# print de getallen deelbaar door 4 en 5, maar niet door 7

i = 1
while i <= 50:
    if ((i % 4 == 0) or (i % 5 == 0)) and (i % 7 != 0):
        print(i)
    i += 1
