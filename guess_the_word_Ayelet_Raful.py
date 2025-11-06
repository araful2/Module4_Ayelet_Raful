"""
This program is a game that lets the user input letter choices and try to guess the correct word. The user can choose from three different categories, and can play
as many times as they would like. There score is kept track of. The user can also choose how many tries they would like to have.
"""
# Importing random so that a word will be chosen at random from the correct category
import random

# Here are three different lists of words that will be chosen at random from depending on the category the user chooses.
animals1 = ["cat", "dog", "bat", "fox", "ant", "cow", "pig", "rat", "bee", "elk", "owl", "ape", "cub", "hen", "kid", "ram", "goat", "gnu", "doe", "kit"]
sports2 = ["golf", "judo", "yoga", "dive", "race", "ski", "run", "gym", "surf", "walk", "arch", "bowl", "pong", "toss", "jump", "dash", "kick", "swim", "bike", "punt"]
foods3 = ["pear", "plum", "kiwi", "corn", "beef", "milk", "egg", "rice", "bean", "taco", "soup", "cake", "fish", "pita", "chop", "roll", "jam", "nut", "fig", "lime"]


"""
This function is the main function that calls all the other functions within it. Besides that, it asks the user to input a letter and runs until the amount of tries 
run out or they guess the correct word- then they are asked if they would like to play again. 
Wins and loss are passed in so that they can be accessed by the play_again function.
"""
def guess_the_word(wins,loss):
    tries = 0
    # Calling the what_level function and storing user's input as hardness so that it can be used as a condition for the while loop.
    hardness = what_level()
    # Calling the categories function and storing the user's input as answer so that it can be used within the while loop.
    answer = categories()
    # Creating an empty list that will keep track of all the letters the user guesses
    user_guesses = []
    # Using a while loop with a condition so that it will only run a certain amount of times within each round.
    while tries < hardness:
        # Asking user to input a letter
        guess = input("Guess a letter ").lower()
        # Checking that user input is a letter

        if not any(char.isalpha() for char in guess):
            print("Please enter a letter")
            continue

        # Checking that user only inputs one letter
        elif len(guess) > 1:
            print("Please enter only one letter")

        # Checking if user repeating a letter already guessed
        elif guess in user_guesses:
            print("You already guessed this letter")
            continue

        else:
            # Appending user's guess to the list
            user_guesses.append(guess)
            tries += 1
            # Calculating remaining tries
            remaining_tries = hardness - tries

            # Checking if user's guess is a letter in the answer.
            for char in answer:
                # If they guessed a correct letter- it will print it
                if char in user_guesses:
                    print(char, end=" ")

                else:
                    # Printing _ for still unguessed letters
                    print("_", end=" ")

            print(f"\n remaining tries: {remaining_tries}")

            # Sorting user's guesses in alphabetical order
            user_guesses.sort()
            print(user_guesses)

            # Checking if user guessed all the letters
            if all(char in user_guesses for char in answer):
                print("Wow, you guessed it!")
                wins += 1
                # Calling play again function to ask user if they would like to play again.
                play_again(wins, loss)
                # Returning so that after play again runs, if user inputs "n" program will exit.
                return

            # If user did not guess the word and ran out of tries then play_again is called.
            elif not all(char in user_guesses for char in answer) and tries == hardness:
                loss += 1
                play_again(wins, loss)
                return


"""
This function asks the user if they would like to play again - if they respond "y", then guess_the_word is called 
and if they respond "n" then the wins and losses are printed and program exits. Passing in wins and loss.
"""
def play_again(wins, loss):
    while True:
        rerun = input("Would you like to play again? y/n ").lower()

        if rerun == "y" :
            # Calling the guess word function if user would like to play again
            guess_the_word(wins, loss)
            return

        elif rerun == "n":
            print(f"Your wins are {wins} and your losses are {loss}")
            print("Exiting")
            return

"""This function asks the user how many tries they would like to have to guess the word. """
def what_level():
    while True:
        try:
            level = int(input("How many tries would you like to have 6/8/10? "))
        except ValueError:
            print("Please enter 6/8/10")
            continue

        # Returning after each statement so that the value stored for hardness will be accessible in the guess_the_word function.
        if level == 10:
            hardness = 10
            return hardness

        elif level == 6:
            hardness = 6
            return hardness

        elif level == 8:
            hardness = 8
            return hardness

        else:
            print("Invalid Input. Please enter 6/8/10")
            continue


""" This function asks the user what category they would like the word to be chosen from. """
def categories():
    while True:
        category = input("Which category would you like a word from? animals/foods/sports ").lower()

        if category == "animals":
            # Storing user input in "answer" and randomizing the choice of the word from the list.
            answer = random.choice(animals1)
            # Returning answer so that answer will be accessible in the guess_the_word_function.
            return answer

        elif category == "sports":
            answer = random.choice(sports2)
            return answer

        elif category == "foods":
            answer = random.choice(foods3)
            return answer

        else:
            print("Invalid input. Please enter animals/foods/sports")
            continue


if __name__ == "__main__":
    # Calling guess_the_word function and passing in staring values for wins and loss.
    guess_the_word(0, 0)



