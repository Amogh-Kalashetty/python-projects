from random import *
import time

print("Please Enter your Name: ")
name = input()
print("Loading.......")
time.sleep(2)


# print("Welcome to the World of Games, " + name)
# time.sleep(2)
# print("Which game do you wanna play? ")
# time.sleep(1)
# print("Enter '1' for Guess Game or Enter '2' for snake")
# option = int(input())




def guess_game():
    print("Welcome to the Guessing world, " + name)
    random_num = randint(0, 101)
    print(random_num)
    chances = 5
    count = 0
    for guesscount in range(6, 1, -1):
        print('Please guess the number')
        chances -= 1
        count += 1
        try:
            guess = int(input())
            if guess > random_num:
                print("Oops! The number is too high!")
                print("Remaining chances: " + str(chances))
            elif guess < random_num:
                print("Oh no! The number is too low!")
                print("Remaining chances: " + str(chances))
            else:
                break
        except:
            print("Only numbers are allowed.")

    if guess == random_num:
        print("Awesome!! You guessed it right in " + str(count) + " guesses, the number is: " + str(random_num))
    elif guesscount == 2:
        print("You ran out of chances :(")
        print("The right answer is: " + str(random_num))


# if option == 1:
#     guess_game()

guess_game()