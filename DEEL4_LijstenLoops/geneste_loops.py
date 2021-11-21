#vb1
for row in range(3):
    for column in range(4):
        print("*", end = "")
    print()


#vb2
for i in range(4):
    for j in range(i+1):
        print("*", end = "")
    print()

#vb3
for i in range(3):
    for j in range(5):
        if j % 2 == 1:
            print("*", end = "")
        else:
            print("0", end = "")
    print()

#controle
for i in range(10):
    for j in range(4):
        print((i + 1) ** (j + 1), end = " ")
    print()

