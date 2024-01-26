# 1. The program randomly selects a secret word from a list of words using the random module.
# 2. The player gets limited chances to win the game.
# 3. When a letter is guessed correctly, that letter becomes visible in the word.
# 4. For convenience, we have given length of word + 2 chances.

import random

secret_words = ["beetle", "whale", "buffalo", "butterfly", "camel", "caterpillar",
                "chameleon", "chicken", "cockroach", "cricket", "crocodile",
                "dolphin", "donkey", "eagle", "elephant", "giraffe", "grasshopper",
                "hamster", "hippopotamus", "horse", "hyena", "kangaroo", "ladybug",
                "lizard", "lobster", "monkey", "mouse", "octopus", "ostrich", "panda",
                "parrot", "peacock", "penguin", "piranha", "rabbit", "reindeer",
                "rhinoceros", "scorpion", "shark", "sheep", "snake", "sparrow", "spider",
                "squirrel", "tiger", "turkey", "turtle", "vulture", "walrus", "zebra"]

selected_word = random.choice(secret_words)
print(f"Chosen Word: {selected_word}")


# Loops through the word adding +1 to the number of letters in order to calculate the number of chances the player will have

length = 0
chances = 0

for character in selected_word:
    length += 1

chances = length + 2
print(f"You have {chances} chances to guess the word")

guesses = "_" * length
print(guesses, "\n")

# Turns guesses into a list since strings are immutable
# This variable will be used to test the letters guessed by the player
guesses_char = list(guesses)


# Asks the player for a letter
# Verifies if the character given is a letter
# Loops through the selected_word checking for the presence of the letter chosen by the player

for n in range(0, chances):
    letter = input(str("Choose a letter: ")).lower()

    if letter.isalpha() is False:
        print("Character must be a letter")
        
    for index, value in enumerate(selected_word):
        if letter == value:
            print(f"Letter found on position number {index + 1} ")
            guesses_char[index] = letter

    print("".join(guesses_char))

    # está indo direto pro input de novo
    # necessário testar se acertou antes
    chances -= 1
    print(f"You have {chances} chances left to guess the word\n")

# Verifies whether the player manage to guess all letters of the word

if chances == 0 and guesses_char != selected_word:
    print("Too bad! Try again.")
elif guesses_char == selected_word: 
    print("Congratulations! You won!")

