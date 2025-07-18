# Write code below 💖
import random

attempts = 10
word_bank = ['help','car','bike','apple','carrot','rain']
word = random.choice(word_bank)
guessword = ['_'] * len(word)

while attempts > 0:
  print('\nCurrentword: ' + ''.join(guessword))
  guess = input("Guess a letter: ").lower()

  if guess in word:
    for i in range(len(word)):
      if word[i] == guess:
        guessword[i] = guess
    print("Great guess")
  else:
    attempts -= 1
    print("Wrong guess!! attempts left:" + str(attempts))

  if '_' not in guessword:
    print("\nCongrats! You guessed the word" + word)
    break
  # if attempts == 0:
  #   print("You lost the game!")





