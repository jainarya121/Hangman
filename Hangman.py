import random
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

word_to_guess = random.choice(words)
word_to_guess_list = list(word_to_guess)
guesses_made = []

display = ["_"] * len(word_to_guess)
print("".join(display))
lives = 6
game_over = False

while "_" in display:
    
    if lives <= 0:
        game_over = True
        break
    else:
        user_input = input("Guess a letter: ").lower().strip()

        while ((not (user_input >= 'a' and user_input <= 'z')) or len(user_input) != 1):
                print("Enter a valid input.")
                user_input = input("Guess a letter: ").lower().strip()

        if user_input in guesses_made:
            print("Repeated input!")
        elif user_input in word_to_guess_list:
            for i in range(len(word_to_guess_list)):
                if word_to_guess_list[i] == user_input:
                    display[i] = user_input
        else:
            lives -= 1

        guesses_made.append(user_input)
        
        print(f"You have {lives} lives left!")
        print(stages[6 - lives])

    print("\n" + "".join(display))

if game_over:
    print("You lost!")
    print(f"It was {word_to_guess}")
else:
    print("You won!")
