import random

guessesTaken = 0
guessesLeft = 6

myName = input("Hello! What's your name? ")

number = random.randrange(1, 21)
print("Well " + myName +", I am thinking of a number between 1 and 20." )

while guessesLeft >0:
    guess = int(input("Take a guess: "))
    guessesTaken += 1
    guessesLeft -=1

    if guess > number:
        print("Your guess is too high.")
    if guess > number:
        print("Your guess is too low.")
    if guess == number:
        "stop loop" #pas aan

if guess == number:
    print("Good job, "+ myName +"! You guessed my number after", guessesTaken, "times.")
else:
    print("Nope. The number I was thinking if was:", number)

