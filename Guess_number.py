import random

print("Guess any number between 1 to 10 ")


def guess_the_number():
    for i in range(1, 4):
        try:
            guessed_number = range(1, 10)
            number = int(random.choice(guessed_number))
            guess = int(input(f"Make your {i} guess = "))

            if guess == number:
                print("You won, that the right number")
            else:
                if guess >= 10:
                    print("please choose the number between 1 to 10")
                    guess_the_number()
                elif guess != number:
                    print("That is the wrong number,Try again")
                    print(f"Correct number was {number} you guessed {guess}")
                else:
                    print("Something went wrong")

        except ValueError:
            print("Please write a valid number between 1 to 10")

    play_again1 = input("Do you want to play again? \n"
                        "Type 'y' for YES and 'n' for NO")
    play_again1.upper()

    while play_again1 == 'Y':
        guess_the_number()
        break


guess_the_number()
