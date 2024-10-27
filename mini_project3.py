import random

# Guesses time is 6
guesses_limit = 6
guesses_remaining = guesses_limit

# The Word List :
word_list = ["rat", "cow", "tiger", "rabbit", "dragon", "snake", "horse", "goat", "monkey", "chicken", "dog", "pig"]

# Select a Random Word :
answer = random.choice(word_list)
# Covert answer to the list ["_", "_", "_"]
answer_list = list(answer)

# Create the current word list
current_word_list = ["_" for _ in answer]

# Create a user_guessed_list
user_guessed_list = []

# Display the Game State:
print("Welcome to Hangman!")
print(f"\nCurrent Word: {' '.join(current_word_list)}")
print("Guessed letters:")
print(f"Incorrect guesses remaining: {guesses_remaining}")

while True:
    if "_" in current_word_list :
        user_guess = input("Guess a letter:").lower()

        # Condition: if guess the same letter, go back the start of the loop
        if user_guess in user_guessed_list :
            print(f"\nYou've already guessed '{user_guess}'. Try agin.")
            continue

        user_guessed_list.append(user_guess) # update the guessed_letters
        guessed_letters = ",".join(user_guessed_list)

        # if guess right
        if user_guess in answer_list :
            for index, letter in enumerate(answer_list): # enumerate : index the letters automatically
                if user_guess == letter :
                    current_word_list[index] = user_guess # update the current word list
            print(f"Good job! '{user_guess}' is in the word.")


        # if guess wrong
        else :
            guesses_remaining -= 1
            print(f"Sorry, '{user_guess}' is not in the word.")

        print(f"\nCurrent word: {' '.join(current_word_list)}")
        print(f"Guessed letters: {guessed_letters}")
        print(f"Incorrect guesses remaining: {guesses_remaining}")

        # run out of chance
        if guesses_remaining == 0:
            print(f"Game over! The word was: {answer}")
            break


    if "_" not in current_word_list:
        print(f"\nCongratulations! You guessed the word: {answer}")
        break


















