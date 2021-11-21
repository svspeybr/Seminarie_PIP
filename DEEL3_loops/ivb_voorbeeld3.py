# vraag naar een strikt positief oneven getal 
# tot zo'n getal ingevoerd wordt

valid = False
while not valid:
    value = input("Enter a positive odd number: ")
    if (value > 0) and (value % 2 == 1):
        #beëindig de loop
        valid = True
    else:
        print("Invalid input. Try again")