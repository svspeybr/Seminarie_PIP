###oef 1 -deel 1
##OPMERKING: achter een of meerdere '#' kan je opmerkingen plaatsen:
##Deze worden niet gelezen door de compiler.
print("Oef1")
print("Hello", "World", "!")

###oef 2
print("Oef2")
#versie 1
print("   +   \n  + +  \n +   + \n+-----+\n| .-. |\n| | | |\n+-+-+-+")
#versie 2: lijn per lijn
print("   +   ",
    "\n  + +  ",
    "\n +   + ",
    "\n+-----+",
    "\n| .-. |",
    "\n| | | |",
    "\n+-+-+-+")

###oef 3
print("Oef3")
m = 234
n = 32
m = m % n % 7
(n + 13)/5 
m = max(n, m ** 3, round(31.45))
print(m, n)

###oef 4
print("Oef4")
a = 2
b = 3

#Gebruik een 'container variabele' c:
c = a
a = b
b = c


#Controle -characters:
print("controle - char") 
bank_account = "IBAN BE37 0006 2100 2100"
card_nr = "CARD 9800 0555 9444 5909 2"
print(bank_account[1:3])
card_nr_digits = card_nr[5:len(card_nr)]
print(card_nr_digits)
print(card_nr_digits[len(card_nr_digits)//2])

##middelste twee cijfers van bank_account:
#cijfers:
bank_account_digits= bank_account[7:9] + bank_account[10:14]+ bank_account[15:19]+ bank_account[20:24]
#midden
print(bank_account_digits[len(bank_account_digits)//2-1]+bank_account_digits[len(bank_account_digits)//2])

