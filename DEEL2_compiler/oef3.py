# oef 3 - deel 2
x = 2
y = -3

# versie 1
s = 0
if x > 0:
    s = s + 1
if y < 0:
    s = s + 1

print(s)

# versie 2
s = 0
if x > 0:
    s = s + 1
elif y < 0:
    s = s + 1

print(s)