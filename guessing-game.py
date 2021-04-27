

import random 

random_int = random.randint(1,100)

print("Welcome to the GUESSING GAME!!\n\n")
print("Let's get down to the rules of this game!!\n")
print("1. The program picks a random number, for which you have to guess what the number is.\n")
print("2. On your first turn, if your guess within 10 of the random number, a string WARM will be printed to let you know you're getting close to the number.\n")
print("3. If your guess is further than 10 away from the number, a string COLD will be printed to let you know you're far away from the number.\n")
print("4. On sussequent turns, if you guess is closer to the number than your previous guess was then a string WARMER! will be displayed.")
print("5. If your current guess is farther from the number than your previous guess then a string COLDER! will be displayed.\n")
start = input("You ready to get started?(y/n): ")

guesses = []

#this is for the first guess
def first_turn():
    while True:
        try:
            guess = int(input("Enter in your guess: "))
        except ValueError:
            print('You must input an integer')
            continue
        else:
            if (guess < 1) or (guess > 100):
                print("OUT OF BOUNDS!!")
            else:
                print("You guessed {} , let's see if you might be right.".format(guess))
                guesses.append(guess)
                if(guesses[-1] == random_int):
                    print("You WON!!!!, it only took {} guesses".format(len(guesses)))
                    break
                elif(abs(random_int - 10) <= guesses[-1] <= (random_int + 10)):
                    print("WARM!")
                    sub_turns()
                    break
                elif(abs(guesses[-1] - random_int) > 10):
                    print("COLD!")
                    sub_turns()
                    break
#this is for subsequent guesses after the first guess
def sub_turns():
    while True:
        sub_guess = int(input("Enter in another guess: "))
        if (sub_guess < 1) or (sub_guess > 100):
            print("OUT OF BOUNDS!")
        else:
            print("You guessed {} , let's see if you are right.".format(sub_guess))
            guesses.append(sub_guess)
            if(guesses[-1] == random_int):
                print("You WON!!!, it only took {} guesses".format(len(guesses)))
                break
            elif((abs(guesses[-1] - random_int)) < abs((guesses[-2] - random_int))):
                print('WARMER!')
            elif((abs(guesses[-1] - random_int)) > abs((guesses[-2] - random_int))):
                print("COLDER")

first_turn()
