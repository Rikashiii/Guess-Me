from art import guess_logo
import random

def easy_mode():
    global OG_NUMBER
    attempts = 10
    while attempts > 0:
        print("You have ",attempts," attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess == OG_NUMBER:
            print ("You got it! The number was ",OG_NUMBER)
            break
        elif guess < OG_NUMBER:
            attempts -= 1
            print("Too Low!")
        elif guess > OG_NUMBER:
            attempts -= 1
            print("Too High!")
    print ("Game over! The number was ",OG_NUMBER) if attempts == 0 else False

def hard_mode():
    global OG_NUMBER
    attempts = 5
    while attempts > 0:
        print("You have ",attempts," attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess == OG_NUMBER:
            print ("You got it! The number was ",OG_NUMBER)
            break
        elif guess < OG_NUMBER:
            attempts -= 1
            print("Too Low!")
        elif guess > OG_NUMBER:
            attempts -= 1
            print("Too High!")
    print ("Game over! The number was ",OG_NUMBER) if attempts == 0 else False
    
#main
print(guess_logo)
print("""Welcome to the 'Guess me' game!
I'm thinking of a number between 1 to 100.""")
difficulty = input("Choose a difficulty: 'easy' or 'hard': ")
OG_NUMBER = random.randint(1,101)
print(OG_NUMBER)
if difficulty == 'easy':
    easy_mode()
elif difficulty == 'hard':
    hard_mode()

