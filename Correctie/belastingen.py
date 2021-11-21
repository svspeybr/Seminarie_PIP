#Belastingen
huw = 0

# 0 = vrijgezel, 1 = gehuwd

inkomen = 42000

# in euro
### Gebruik best een nieuwe variabele. Je mag inkomen inderdaad overschrijven.
### Maar een nieuwe variabele leest gemakkelijke
belas = 0

if huw == 0:

    if inkomen <= 32000:
        ###Je mag niet zomaar een variabele afkorten 
        ### --> je hebt 'inkomen' gebruikt, dus 'ink'wordt 'inkomen'
        belas = inkomen * 0.1
    ###puntjes na else en nieuwe lijn
    else:
        # geen 25 percent meer 
        ### bewerkingen werd aangepast: 10% belasting op de eerste 32 000, 
        ###van het overige bedrag (inkomen -32000) --> 25% belastingen
        belas = 0.25*(inkomen - 32000) +3200 
###puntjes na else en nieuwe lijn
else:
    if inkomen <= 64000:
        ###'ink'wordt 'inkomen'
        belas = inkomen*0.1

    else: 
        ###
        belas = 0.25*(inkomen-64000)+6400  
### haakjes na print (en inkomen --> belas)
print(belas)