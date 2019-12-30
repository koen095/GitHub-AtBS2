# Game for guessing a random number
import random
number = random.randint(1, 20)

print('Welcome to the guess the number game!')
print('Please, take a guess between 1 and 20')

for guessesTaken in range(1, 7):
    guess = int(input())
    if guess != number:
        print("I'm thinking of a different number")
    elif guess == number:
        print("you guessed " + str(guess) + ", the secret number was " + str(number) + ", you guessed correct!")
print("Unluckyy, the right number was " + str(number))